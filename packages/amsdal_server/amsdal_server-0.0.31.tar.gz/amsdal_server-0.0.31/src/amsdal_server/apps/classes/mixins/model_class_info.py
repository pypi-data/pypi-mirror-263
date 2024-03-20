from amsdal_models.classes.manager import ClassManager
from amsdal_models.classes.model import Model
from amsdal_models.querysets.base_queryset import QuerySet
from amsdal_utils.models.enums import SchemaTypes
from amsdal_utils.query.utils import Q

from amsdal_server.apps.classes.errors import ClassNotFoundError


class ModelClassMixin:
    @classmethod
    def get_model_class_by_name(cls, class_name: str) -> type[Model]:
        class_item: Model | None = cls.get_class_objects_qs().latest().filter(title=class_name).first().execute()

        if not class_item:
            msg = f'Class not found: {class_name}'
            raise ClassNotFoundError(class_name, msg)

        return cls.get_model_class(class_item)

    @classmethod
    def get_model_class(cls, class_item: Model) -> type[Model]:
        class_manager = ClassManager()
        model_class = class_manager.import_model_class(
            class_item.title,
            class_item.get_metadata().class_schema_type,
        )

        return model_class

    @classmethod
    def get_class_objects_qs(cls) -> QuerySet:  # type: ignore[type-arg]
        class_manager = ClassManager()
        class_object: type[Model] = class_manager.import_model_class('ClassObject', SchemaTypes.CORE)

        return class_object.objects.filter(
            (
                Q(_metadata__class_schema_type=SchemaTypes.CONTRIB)
                | Q(_metadata__class_schema_type=SchemaTypes.USER)
                | Q(title='File')  # ugly hack
            ),
            _metadata__is_deleted=False,
            _metadata__next_version__isnull=True,
        )
