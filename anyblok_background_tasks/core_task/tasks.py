"""demo Example model, this model is goging to create table at startup
"""
from typing import TYPE_CHECKING

from anyblok import Declarations
from anyblok.column import Integer, Selection, String

Model = Declarations.Model

if TYPE_CHECKING:
    from typing import Dict


@Declarations.register(Model.System)
class Tasks(Declarations.Mixin.TrackModel):
    """Abstract polymorphic base class, each instance would represent a task.

    You have to inherit this Tasks in order to implement its behaviour::

        @Declarations.register(Model.System.Tasks)
        class MyTask:

            TASK_TYPE = "MY-TASK"

            def execute(self, dry_run: "bool" = False)-> None:
                # TODO: implement task behaviours


        @Declarations.register(Model.System)
        class Tasks:
            # add extrat TASK_TYPE

            @classmethod
            def get_task_types(cls) -> "dict[str,str]":
                res = super(Tasks, cls).get_task_types()
                res.update(dict(MYTASK='My Task'))
                return res

    """

    TASK_TYPE = None

    id: "int" = Integer(primary_key=True)
    code: "str" = String(label="Code", unique=True, nullable=False)
    task_type: "str" = Selection(selections="get_task_types")

    @classmethod
    def define_mapper_args(cls) -> "Dict[str,str]":
        mapper_args = super(Tasks, cls).define_mapper_args()
        if cls.__registry_name__ == "Model.System.Tasks":
            mapper_args.update({"polymorphic_on": cls.task_type})

        mapper_args.update({"polymorphic_identity": cls.TASK_TYPE})
        return mapper_args

    @classmethod
    def get_task_types(cls) -> "Dict[str,str]":
        """list possible task_type values"""
        return dict()

    def execute(self, dry_run: "bool" = False) -> None:
        """Run the instantiated class, must be implements in subclass"""
        raise NotImplementedError(
            "Creating task directly from System.Tasks class "
            "is Forbidden. Please use a specialized one."
        )
