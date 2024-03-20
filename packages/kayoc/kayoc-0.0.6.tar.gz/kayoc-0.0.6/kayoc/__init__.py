from dataclasses import dataclass
from typing import Optional, List, Union, Literal




@dataclass
class KayocError:
    succes: bool
    message: str
    done: bool
    error: str

    @classmethod
    def from_json(cls, data: dict) -> "KayocError":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
            error = data["error"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["error"] = self.error

        return data

    @classmethod
    def example(cls) -> 'KayocError':
        return cls(
            succes=True,
            message="Hi, its kayoc here 😉💅",
            done=False,
            error="The only thing your eyes haven't told me is your name 👀🤔",
        )

@dataclass
class CreateDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "CreateDatabaseRequest":
        return cls(
            database_name = data["database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> 'CreateDatabaseRequest':
        return cls(
            database_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
        )

@dataclass
class DatabasePermission:
    user_id: int
    user_email: str
    database_id: int
    type: str

    @classmethod
    def from_json(cls, data: dict) -> "DatabasePermission":
        return cls(
            user_id = data["user_id"],
            user_email = data["user_email"],
            database_id = data["database_id"],
            type = data["type"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["user_id"] = self.user_id
        data["user_email"] = self.user_email
        data["database_id"] = self.database_id
        data["type"] = self.type

        return data

    @classmethod
    def example(cls) -> 'DatabasePermission':
        return cls(
            user_id=666,
            user_email="The only thing your eyes haven't told me is your name 👀🤔",
            database_id=69,
            type="You've got character! ㍼🥴",
        )

@dataclass
class CreateDatabaseResponse:
    database_id: int
    permissions: list[DatabasePermission]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "CreateDatabaseResponse":
        return cls(
            database_id = data["database_id"],
            permissions = [DatabasePermission.from_json(item) for item in data["permissions"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_id"] = self.database_id
        data["permissions"] = [DatabasePermission.to_json(item) for item in self.permissions]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'CreateDatabaseResponse':
        return cls(
            database_id=69,
            permissions=[DatabasePermission.example(), DatabasePermission.example(), DatabasePermission.example(), DatabasePermission.example(), DatabasePermission.example(), DatabasePermission.example()],
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class DeleteDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "DeleteDatabaseRequest":
        return cls(
            database_name = data["database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> 'DeleteDatabaseRequest':
        return cls(
            database_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )

@dataclass
class DeleteDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DeleteDatabaseResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DeleteDatabaseResponse':
        return cls(
            succes=True,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=True,
        )

@dataclass
class DatabaseInfoRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseInfoRequest":
        return cls(
            database_name = data["database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> 'DatabaseInfoRequest':
        return cls(
            database_name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
        )

@dataclass
class UserDatabasePermissionInfo:
    user_id: int
    user_email: str
    type: str

    @classmethod
    def from_json(cls, data: dict) -> "UserDatabasePermissionInfo":
        return cls(
            user_id = data["user_id"],
            user_email = data["user_email"],
            type = data["type"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["user_id"] = self.user_id
        data["user_email"] = self.user_email
        data["type"] = self.type

        return data

    @classmethod
    def example(cls) -> 'UserDatabasePermissionInfo':
        return cls(
            user_id=420,
            user_email="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            type="Just like a fine wine, you get better with age 🍷👵",
        )

@dataclass
class DataBaseInfoSubFolder:
    folder_id: int
    name: str
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "DataBaseInfoSubFolder":
        return cls(
            folder_id = data["folder_id"],
            name = data["name"],
            description = data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name
        
        if self.description is not None:
            data["description"] = self.description


        return data

    @classmethod
    def example(cls) -> 'DataBaseInfoSubFolder':
        return cls(
            folder_id=69,
            name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            description=None,
        )

@dataclass
class DatabaseInfoItem:
    item_id: int
    name: str

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseInfoItem":
        return cls(
            item_id = data["item_id"],
            name = data["name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id
        data["name"] = self.name

        return data

    @classmethod
    def example(cls) -> 'DatabaseInfoItem':
        return cls(
            item_id=420,
            name="You've got character! ㍼🥴",
        )

@dataclass
class DatabaseInfoFolder:
    folder_id: int
    name: str
    subfolders: list[DataBaseInfoSubFolder]
    items: list[DatabaseInfoItem]
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseInfoFolder":
        return cls(
            folder_id = data["folder_id"],
            name = data["name"],
            subfolders = [DataBaseInfoSubFolder.from_json(item) for item in data["subfolders"]],
            items = [DatabaseInfoItem.from_json(item) for item in data["items"]],
            description = data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name
        data["subfolders"] = [DataBaseInfoSubFolder.to_json(item) for item in self.subfolders]
        data["items"] = [DatabaseInfoItem.to_json(item) for item in self.items]
        
        if self.description is not None:
            data["description"] = self.description


        return data

    @classmethod
    def example(cls) -> 'DatabaseInfoFolder':
        return cls(
            folder_id=420,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            subfolders=[DataBaseInfoSubFolder.example(), DataBaseInfoSubFolder.example(), DataBaseInfoSubFolder.example(), DataBaseInfoSubFolder.example(), DataBaseInfoSubFolder.example()],
            items=[DatabaseInfoItem.example(), DatabaseInfoItem.example(), DatabaseInfoItem.example(), DatabaseInfoItem.example(), DatabaseInfoItem.example(), DatabaseInfoItem.example(), DatabaseInfoItem.example()],
            description=None,
        )

@dataclass
class DateTime:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    @classmethod
    def from_json(cls, data: dict) -> "DateTime":
        return cls(
            year = data["year"],
            month = data["month"],
            day = data["day"],
            hour = data["hour"],
            minute = data["minute"],
            second = data["second"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["year"] = self.year
        data["month"] = self.month
        data["day"] = self.day
        data["hour"] = self.hour
        data["minute"] = self.minute
        data["second"] = self.second

        return data

    @classmethod
    def example(cls) -> 'DateTime':
        return cls(
            year=420,
            month=69,
            day=420,
            hour=666,
            minute=69,
            second=420,
        )

@dataclass
class DatabaseInfoBuild:
    build_id: int
    name: str
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseInfoBuild":
        return cls(
            build_id = data["build_id"],
            name = data["name"],
            created_at = DateTime.from_json(data['created_at']),
        )

    def to_json(self) -> dict:
        data = dict()
        data["build_id"] = self.build_id
        data["name"] = self.name
        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> 'DatabaseInfoBuild':
        return cls(
            build_id=666,
            name="Wanna go out? No strings attached 🍆🍑",
            created_at=DateTime.example(),
        )

@dataclass
class DatabaseInfoQuestion:
    question_id: int
    name: str
    build_name: str
    build_id: int
    created_at: DateTime
    first_message: str

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseInfoQuestion":
        return cls(
            question_id = data["question_id"],
            name = data["name"],
            build_name = data["build_name"],
            build_id = data["build_id"],
            created_at = DateTime.from_json(data['created_at']),
            first_message = data["first_message"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["question_id"] = self.question_id
        data["name"] = self.name
        data["build_name"] = self.build_name
        data["build_id"] = self.build_id
        data["created_at"] = self.created_at.to_json()
        data["first_message"] = self.first_message

        return data

    @classmethod
    def example(cls) -> 'DatabaseInfoQuestion':
        return cls(
            question_id=69,
            name="You've got character! ㍼🥴",
            build_name="Just like a fine wine, you get better with age 🍷👵",
            build_id=420,
            created_at=DateTime.example(),
            first_message="Just like a fine wine, you get better with age 🍷👵",
        )

@dataclass
class DatabaseInfoResponse:
    database_id: int
    name: str
    description: Optional[str]
    is_public: bool
    permissions: list[UserDatabasePermissionInfo]
    folder: DatabaseInfoFolder
    builds: list[DatabaseInfoBuild]
    questions: list[DatabaseInfoQuestion]
    created_at: DateTime
    size_bytes: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseInfoResponse":
        return cls(
            database_id = data["database_id"],
            name = data["name"],
            description = data["description"] if "description" in data else None,
            is_public = data["is_public"],
            permissions = [UserDatabasePermissionInfo.from_json(item) for item in data["permissions"]],
            folder = DatabaseInfoFolder.from_json(data['folder']),
            builds = [DatabaseInfoBuild.from_json(item) for item in data["builds"]],
            questions = [DatabaseInfoQuestion.from_json(item) for item in data["questions"]],
            created_at = DateTime.from_json(data['created_at']),
            size_bytes = data["size_bytes"],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name
        
        if self.description is not None:
            data["description"] = self.description

        data["is_public"] = self.is_public
        data["permissions"] = [UserDatabasePermissionInfo.to_json(item) for item in self.permissions]
        data["folder"] = self.folder.to_json()
        data["builds"] = [DatabaseInfoBuild.to_json(item) for item in self.builds]
        data["questions"] = [DatabaseInfoQuestion.to_json(item) for item in self.questions]
        data["created_at"] = self.created_at.to_json()
        data["size_bytes"] = self.size_bytes
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DatabaseInfoResponse':
        return cls(
            database_id=69,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            description="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            is_public=False,
            permissions=[UserDatabasePermissionInfo.example(), UserDatabasePermissionInfo.example(), UserDatabasePermissionInfo.example(), UserDatabasePermissionInfo.example()],
            folder=DatabaseInfoFolder.example(),
            builds=[DatabaseInfoBuild.example(), DatabaseInfoBuild.example(), DatabaseInfoBuild.example(), DatabaseInfoBuild.example()],
            questions=[DatabaseInfoQuestion.example(), DatabaseInfoQuestion.example(), DatabaseInfoQuestion.example(), DatabaseInfoQuestion.example(), DatabaseInfoQuestion.example(), DatabaseInfoQuestion.example(), DatabaseInfoQuestion.example()],
            created_at=DateTime.example(),
            size_bytes=666,
            succes=False,
            message="Hi, its kayoc here 😉💅",
            done=False,
        )

@dataclass
class RenameDatabaseRequest:
    database_name: str
    new_name: str

    @classmethod
    def from_json(cls, data: dict) -> "RenameDatabaseRequest":
        return cls(
            database_name = data["database_name"],
            new_name = data["new_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> 'RenameDatabaseRequest':
        return cls(
            database_name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            new_name="I'm not a photographer, but I can picture us together 📸👫",
        )

@dataclass
class RenameDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "RenameDatabaseResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'RenameDatabaseResponse':
        return cls(
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )

@dataclass
class DatabaseUpdateDescriptionRequest:
    database_name: str
    new_description: str

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseUpdateDescriptionRequest":
        return cls(
            database_name = data["database_name"],
            new_description = data["new_description"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name
        data["new_description"] = self.new_description

        return data

    @classmethod
    def example(cls) -> 'DatabaseUpdateDescriptionRequest':
        return cls(
            database_name="Just like a fine wine, you get better with age 🍷👵",
            new_description="I'm not a photographer, but I can picture us together 📸👫",
        )

@dataclass
class DatabaseUpdateDescriptionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseUpdateDescriptionResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DatabaseUpdateDescriptionResponse':
        return cls(
            succes=True,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=True,
        )

@dataclass
class DatabaseBrowseRequest:
    fuzzy_database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseBrowseRequest":
        return cls(
            fuzzy_database_name = data["fuzzy_database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["fuzzy_database_name"] = self.fuzzy_database_name

        return data

    @classmethod
    def example(cls) -> 'DatabaseBrowseRequest':
        return cls(
            fuzzy_database_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
        )

@dataclass
class BrowseDatabaseInfo:
    database_id: int
    name: str
    owner_email: str
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "BrowseDatabaseInfo":
        return cls(
            database_id = data["database_id"],
            name = data["name"],
            owner_email = data["owner_email"],
            description = data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name
        data["owner_email"] = self.owner_email
        
        if self.description is not None:
            data["description"] = self.description


        return data

    @classmethod
    def example(cls) -> 'BrowseDatabaseInfo':
        return cls(
            database_id=69,
            name="I'm not a photographer, but I can picture us together 📸👫",
            owner_email="Wanna go out? No strings attached 🍆🍑",
            description="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
        )

@dataclass
class DatabaseBrowseResponse:
    databases: list[BrowseDatabaseInfo]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseBrowseResponse":
        return cls(
            databases = [BrowseDatabaseInfo.from_json(item) for item in data["databases"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["databases"] = [BrowseDatabaseInfo.to_json(item) for item in self.databases]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DatabaseBrowseResponse':
        return cls(
            databases=[BrowseDatabaseInfo.example(), BrowseDatabaseInfo.example(), BrowseDatabaseInfo.example(), BrowseDatabaseInfo.example(), BrowseDatabaseInfo.example(), BrowseDatabaseInfo.example()],
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )

@dataclass
class DatabaseUpdatePermissionRequest:
    database_name: str
    user_email: str
    new_permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseUpdatePermissionRequest":
        return cls(
            database_name = data["database_name"],
            user_email = data["user_email"],
            new_permission = data["new_permission"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name
        data["user_email"] = self.user_email
        data["new_permission"] = self.new_permission

        return data

    @classmethod
    def example(cls) -> 'DatabaseUpdatePermissionRequest':
        return cls(
            database_name="Hi, its kayoc here 😉💅",
            user_email="You've got character! ㍼🥴",
            new_permission="delete",
        )

@dataclass
class DatabaseUpdatePermissionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseUpdatePermissionResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DatabaseUpdatePermissionResponse':
        return cls(
            succes=True,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=False,
        )

@dataclass
class PublishDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "PublishDatabaseRequest":
        return cls(
            database_name = data["database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> 'PublishDatabaseRequest':
        return cls(
            database_name="Wanna go out? No strings attached 🍆🍑",
        )

@dataclass
class PublishDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "PublishDatabaseResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'PublishDatabaseResponse':
        return cls(
            succes=True,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )

@dataclass
class UnpublishDatabaseRequest:
    database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "UnpublishDatabaseRequest":
        return cls(
            database_name = data["database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> 'UnpublishDatabaseRequest':
        return cls(
            database_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )

@dataclass
class UnpublishDatabaseResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UnpublishDatabaseResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UnpublishDatabaseResponse':
        return cls(
            succes=False,
            message="Just like a fine wine, you get better with age 🍷👵",
            done=True,
        )

@dataclass
class DatabaseListDatabase:
    database_id: int
    name: str
    description: Optional[str]
    is_public: bool
    created_at: DateTime
    size_bytes: int
    nitems: int
    nbuilds: int
    nquestions: int

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseListDatabase":
        return cls(
            database_id = data["database_id"],
            name = data["name"],
            description = data["description"] if "description" in data else None,
            is_public = data["is_public"],
            created_at = DateTime.from_json(data['created_at']),
            size_bytes = data["size_bytes"],
            nitems = data["nitems"],
            nbuilds = data["nbuilds"],
            nquestions = data["nquestions"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name
        
        if self.description is not None:
            data["description"] = self.description

        data["is_public"] = self.is_public
        data["created_at"] = self.created_at.to_json()
        data["size_bytes"] = self.size_bytes
        data["nitems"] = self.nitems
        data["nbuilds"] = self.nbuilds
        data["nquestions"] = self.nquestions

        return data

    @classmethod
    def example(cls) -> 'DatabaseListDatabase':
        return cls(
            database_id=69,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            description=None,
            is_public=True,
            created_at=DateTime.example(),
            size_bytes=666,
            nitems=69,
            nbuilds=666,
            nquestions=69,
        )

@dataclass
class DatabaseListResponse:
    databases: list[DatabaseListDatabase]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DatabaseListResponse":
        return cls(
            databases = [DatabaseListDatabase.from_json(item) for item in data["databases"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["databases"] = [DatabaseListDatabase.to_json(item) for item in self.databases]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DatabaseListResponse':
        return cls(
            databases=[DatabaseListDatabase.example(), DatabaseListDatabase.example(), DatabaseListDatabase.example()],
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )

@dataclass
class QuestionInfoRequest:
    question_id: int

    @classmethod
    def from_json(cls, data: dict) -> "QuestionInfoRequest":
        return cls(
            question_id = data["question_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["question_id"] = self.question_id

        return data

    @classmethod
    def example(cls) -> 'QuestionInfoRequest':
        return cls(
            question_id=666,
        )

@dataclass
class MessageRelevantText:
    id: int
    item_id: int

    @classmethod
    def from_json(cls, data: dict) -> "MessageRelevantText":
        return cls(
            id = data["id"],
            item_id = data["item_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["id"] = self.id
        data["item_id"] = self.item_id

        return data

    @classmethod
    def example(cls) -> 'MessageRelevantText':
        return cls(
            id=666,
            item_id=666,
        )

@dataclass
class AnswerInfoRating:
    rating: Literal["down", "neutral", "up"]
    user_id: int
    user_email: str

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfoRating":
        return cls(
            rating = data["rating"],
            user_id = data["user_id"],
            user_email = data["user_email"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["rating"] = self.rating
        data["user_id"] = self.user_id
        data["user_email"] = self.user_email

        return data

    @classmethod
    def example(cls) -> 'AnswerInfoRating':
        return cls(
            rating="down",
            user_id=666,
            user_email="The only thing your eyes haven't told me is your name 👀🤔",
        )

@dataclass
class AnswerInfo:
    content: str
    explanation: str
    ratings: list[AnswerInfoRating]
    answer_id: int

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfo":
        return cls(
            content = data["content"],
            explanation = data["explanation"],
            ratings = [AnswerInfoRating.from_json(item) for item in data["ratings"]],
            answer_id = data["answer_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["content"] = self.content
        data["explanation"] = self.explanation
        data["ratings"] = [AnswerInfoRating.to_json(item) for item in self.ratings]
        data["answer_id"] = self.answer_id

        return data

    @classmethod
    def example(cls) -> 'AnswerInfo':
        return cls(
            content="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            explanation="Just like a fine wine, you get better with age 🍷👵",
            ratings=[AnswerInfoRating.example(), AnswerInfoRating.example(), AnswerInfoRating.example(), AnswerInfoRating.example(), AnswerInfoRating.example(), AnswerInfoRating.example()],
            answer_id=69,
        )

@dataclass
class MessageInfo:
    relevant_texts: list[MessageRelevantText]
    answer: AnswerInfo
    content: str
    created_at: DateTime
    message_id: int

    @classmethod
    def from_json(cls, data: dict) -> "MessageInfo":
        return cls(
            relevant_texts = [MessageRelevantText.from_json(item) for item in data["relevant_texts"]],
            answer = AnswerInfo.from_json(data['answer']),
            content = data["content"],
            created_at = DateTime.from_json(data['created_at']),
            message_id = data["message_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["relevant_texts"] = [MessageRelevantText.to_json(item) for item in self.relevant_texts]
        data["answer"] = self.answer.to_json()
        data["content"] = self.content
        data["created_at"] = self.created_at.to_json()
        data["message_id"] = self.message_id

        return data

    @classmethod
    def example(cls) -> 'MessageInfo':
        return cls(
            relevant_texts=[MessageRelevantText.example(), MessageRelevantText.example(), MessageRelevantText.example(), MessageRelevantText.example(), MessageRelevantText.example(), MessageRelevantText.example(), MessageRelevantText.example()],
            answer=AnswerInfo.example(),
            content="The only thing your eyes haven't told me is your name 👀🤔",
            created_at=DateTime.example(),
            message_id=666,
        )

@dataclass
class QuestionInfoResponse:
    question_id: int
    name: Optional[str]
    created_at: DateTime
    messages: list[MessageInfo]
    build_name: str
    build_id: int
    database_name: str
    database_id: int
    user_id: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "QuestionInfoResponse":
        return cls(
            question_id = data["question_id"],
            name = data["name"] if "name" in data else None,
            created_at = DateTime.from_json(data['created_at']),
            messages = [MessageInfo.from_json(item) for item in data["messages"]],
            build_name = data["build_name"],
            build_id = data["build_id"],
            database_name = data["database_name"],
            database_id = data["database_id"],
            user_id = data["user_id"],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["question_id"] = self.question_id
        
        if self.name is not None:
            data["name"] = self.name

        data["created_at"] = self.created_at.to_json()
        data["messages"] = [MessageInfo.to_json(item) for item in self.messages]
        data["build_name"] = self.build_name
        data["build_id"] = self.build_id
        data["database_name"] = self.database_name
        data["database_id"] = self.database_id
        data["user_id"] = self.user_id
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'QuestionInfoResponse':
        return cls(
            question_id=666,
            name=None,
            created_at=DateTime.example(),
            messages=[MessageInfo.example(), MessageInfo.example(), MessageInfo.example()],
            build_name="Just like a fine wine, you get better with age 🍷👵",
            build_id=420,
            database_name="Wanna go out? No strings attached 🍆🍑",
            database_id=420,
            user_id=666,
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class QuestionListQuestion:
    name: str
    question_id: int
    created_at: DateTime
    nmessages: int
    database_name: str
    build_name: str

    @classmethod
    def from_json(cls, data: dict) -> "QuestionListQuestion":
        return cls(
            name = data["name"],
            question_id = data["question_id"],
            created_at = DateTime.from_json(data['created_at']),
            nmessages = data["nmessages"],
            database_name = data["database_name"],
            build_name = data["build_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["name"] = self.name
        data["question_id"] = self.question_id
        data["created_at"] = self.created_at.to_json()
        data["nmessages"] = self.nmessages
        data["database_name"] = self.database_name
        data["build_name"] = self.build_name

        return data

    @classmethod
    def example(cls) -> 'QuestionListQuestion':
        return cls(
            name="I'm not a photographer, but I can picture us together 📸👫",
            question_id=420,
            created_at=DateTime.example(),
            nmessages=420,
            database_name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            build_name="The only thing your eyes haven't told me is your name 👀🤔",
        )

@dataclass
class QuestionListResponse:
    questions: list[QuestionListQuestion]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "QuestionListResponse":
        return cls(
            questions = [QuestionListQuestion.from_json(item) for item in data["questions"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["questions"] = [QuestionListQuestion.to_json(item) for item in self.questions]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'QuestionListResponse':
        return cls(
            questions=[QuestionListQuestion.example(), QuestionListQuestion.example(), QuestionListQuestion.example()],
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=False,
        )

@dataclass
class UpdateQuestionNameRequest:
    question_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict) -> "UpdateQuestionNameRequest":
        return cls(
            question_id = data["question_id"],
            new_name = data["new_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["question_id"] = self.question_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> 'UpdateQuestionNameRequest':
        return cls(
            question_id=666,
            new_name="Wanna go out? No strings attached 🍆🍑",
        )

@dataclass
class UpdateQuestionNameResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UpdateQuestionNameResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UpdateQuestionNameResponse':
        return cls(
            succes=False,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=False,
        )

@dataclass
class RerankConfig:

    @classmethod
    def from_json(cls, data: dict) -> "RerankConfig":
        return cls(
        )

    def to_json(self) -> dict:
        data = dict()

        return data

    @classmethod
    def example(cls) -> 'RerankConfig':
        return cls(
        )

@dataclass
class AnswerConfig:
    model: Literal["openai", "mixtral", "idk"]
    rerank_config: RerankConfig

    @classmethod
    def from_json(cls, data: dict) -> "AnswerConfig":
        return cls(
            model = data["model"],
            rerank_config = RerankConfig.from_json(data['rerank_config']),
        )

    def to_json(self) -> dict:
        data = dict()
        data["model"] = self.model
        data["rerank_config"] = self.rerank_config.to_json()

        return data

    @classmethod
    def example(cls) -> 'AnswerConfig':
        return cls(
            model="idk",
            rerank_config=RerankConfig.example(),
        )

@dataclass
class EmbedConfig:
    blur: bool
    blur_reach: int
    model: Literal["openai-small", "openai-large", "mistral", "random"]
    chunk_size: int
    chunk_overlap: int

    @classmethod
    def from_json(cls, data: dict) -> "EmbedConfig":
        return cls(
            blur = data["blur"],
            blur_reach = data["blur_reach"],
            model = data["model"],
            chunk_size = data["chunk_size"],
            chunk_overlap = data["chunk_overlap"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["blur"] = self.blur
        data["blur_reach"] = self.blur_reach
        data["model"] = self.model
        data["chunk_size"] = self.chunk_size
        data["chunk_overlap"] = self.chunk_overlap

        return data

    @classmethod
    def example(cls) -> 'EmbedConfig':
        return cls(
            blur=False,
            blur_reach=666,
            model="mistral",
            chunk_size=420,
            chunk_overlap=666,
        )

@dataclass
class RetrieveConfig:
    embed_config: EmbedConfig
    top_k: int

    @classmethod
    def from_json(cls, data: dict) -> "RetrieveConfig":
        return cls(
            embed_config = EmbedConfig.from_json(data['embed_config']),
            top_k = data["top_k"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["embed_config"] = self.embed_config.to_json()
        data["top_k"] = self.top_k

        return data

    @classmethod
    def example(cls) -> 'RetrieveConfig':
        return cls(
            embed_config=EmbedConfig.example(),
            top_k=420,
        )

@dataclass
class CreateAnswerRequest:
    question: str
    database_name: str
    question_id: Optional[int]
    build_name: Optional[str]
    keywords: Optional[list[str]]
    top_k: Optional[int]
    answer_config: Optional[AnswerConfig]
    retrieve_config: Optional[RetrieveConfig]
    rerank_config: Optional[RerankConfig]

    @classmethod
    def from_json(cls, data: dict) -> "CreateAnswerRequest":
        return cls(
            question = data["question"],
            database_name = data["database_name"],
            question_id = data["question_id"] if "question_id" in data else None,
            build_name = data["build_name"] if "build_name" in data else None,
            keywords = data["keywords"] if "keywords" in data else None,
            top_k = data["top_k"] if "top_k" in data else None,
            answer_config = data["answer_config"] if "answer_config" in data else None,
            retrieve_config = data["retrieve_config"] if "retrieve_config" in data else None,
            rerank_config = data["rerank_config"] if "rerank_config" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["question"] = self.question
        data["database_name"] = self.database_name
        
        if self.question_id is not None:
            data["question_id"] = self.question_id

        
        if self.build_name is not None:
            data["build_name"] = self.build_name

        
        if self.keywords is not None:
            data["keywords"] = self.keywords

        
        if self.top_k is not None:
            data["top_k"] = self.top_k

        
        if self.answer_config is not None:
            data["answer_config"] = self.answer_config

        
        if self.retrieve_config is not None:
            data["retrieve_config"] = self.retrieve_config

        
        if self.rerank_config is not None:
            data["rerank_config"] = self.rerank_config


        return data

    @classmethod
    def example(cls) -> 'CreateAnswerRequest':
        return cls(
            question="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            database_name="I'm not a photographer, but I can picture us together 📸👫",
            question_id=None,
            build_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            keywords=None,
            top_k=None,
            answer_config=None,
            retrieve_config=None,
            rerank_config=RerankConfig.example(),
        )

@dataclass
class AnswerResultRelevantPart:
    item_id: int
    url: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "AnswerResultRelevantPart":
        return cls(
            item_id = data["item_id"],
            url = data["url"] if "url" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id
        
        if self.url is not None:
            data["url"] = self.url


        return data

    @classmethod
    def example(cls) -> 'AnswerResultRelevantPart':
        return cls(
            item_id=420,
            url=None,
        )

@dataclass
class CreateAnswerResponse:
    answer: str
    context: str
    explanation: str
    question_id: int
    answer_id: int
    message_id: int
    relevant_parts: list[AnswerResultRelevantPart]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "CreateAnswerResponse":
        return cls(
            answer = data["answer"],
            context = data["context"],
            explanation = data["explanation"],
            question_id = data["question_id"],
            answer_id = data["answer_id"],
            message_id = data["message_id"],
            relevant_parts = [AnswerResultRelevantPart.from_json(item) for item in data["relevant_parts"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["answer"] = self.answer
        data["context"] = self.context
        data["explanation"] = self.explanation
        data["question_id"] = self.question_id
        data["answer_id"] = self.answer_id
        data["message_id"] = self.message_id
        data["relevant_parts"] = [AnswerResultRelevantPart.to_json(item) for item in self.relevant_parts]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'CreateAnswerResponse':
        return cls(
            answer="Just like a fine wine, you get better with age 🍷👵",
            context="Just like a fine wine, you get better with age 🍷👵",
            explanation="I'm not a photographer, but I can picture us together 📸👫",
            question_id=69,
            answer_id=666,
            message_id=666,
            relevant_parts=[AnswerResultRelevantPart.example(), AnswerResultRelevantPart.example()],
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=True,
        )

@dataclass
class CreateAnswerUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "CreateAnswerUpdateResponse":
        return cls(
            task = data["task"],
            total = data["total"] if "total" in data else None,
            count = data["count"] if "count" in data else None,
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["task"] = self.task
        
        if self.total is not None:
            data["total"] = self.total

        
        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'CreateAnswerUpdateResponse':
        return cls(
            task="Just like a fine wine, you get better with age 🍷👵",
            total=666,
            count=666,
            succes=False,
            message="You've got character! ㍼🥴",
            done=False,
        )

@dataclass
class AnswerInfoRequest:
    answer_id: int

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfoRequest":
        return cls(
            answer_id = data["answer_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["answer_id"] = self.answer_id

        return data

    @classmethod
    def example(cls) -> 'AnswerInfoRequest':
        return cls(
            answer_id=666,
        )

@dataclass
class AnswerInfoRating:
    user_email: str
    user_id: int
    rating: Literal["down", "neutral", "up"]

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfoRating":
        return cls(
            user_email = data["user_email"],
            user_id = data["user_id"],
            rating = data["rating"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["user_email"] = self.user_email
        data["user_id"] = self.user_id
        data["rating"] = self.rating

        return data

    @classmethod
    def example(cls) -> 'AnswerInfoRating':
        return cls(
            user_email="Hi, its kayoc here 😉💅",
            user_id=666,
            rating="up",
        )

@dataclass
class AnswerInfoRelevantPartRating:
    user_email: str
    user_id: int
    rating: Literal["relevant", "irrelevant", "neutral"]

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfoRelevantPartRating":
        return cls(
            user_email = data["user_email"],
            user_id = data["user_id"],
            rating = data["rating"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["user_email"] = self.user_email
        data["user_id"] = self.user_id
        data["rating"] = self.rating

        return data

    @classmethod
    def example(cls) -> 'AnswerInfoRelevantPartRating':
        return cls(
            user_email="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            user_id=666,
            rating="neutral",
        )

@dataclass
class AnswerInfoRelevantPart:
    part_id: int
    item_id: int
    content: str
    ratings: list[AnswerInfoRelevantPartRating]

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfoRelevantPart":
        return cls(
            part_id = data["part_id"],
            item_id = data["item_id"],
            content = data["content"],
            ratings = [AnswerInfoRelevantPartRating.from_json(item) for item in data["ratings"]],
        )

    def to_json(self) -> dict:
        data = dict()
        data["part_id"] = self.part_id
        data["item_id"] = self.item_id
        data["content"] = self.content
        data["ratings"] = [AnswerInfoRelevantPartRating.to_json(item) for item in self.ratings]

        return data

    @classmethod
    def example(cls) -> 'AnswerInfoRelevantPart':
        return cls(
            part_id=420,
            item_id=666,
            content="Wanna go out? No strings attached 🍆🍑",
            ratings=[AnswerInfoRelevantPartRating.example()],
        )

@dataclass
class AnswerInfoResponse:
    answer_id: int
    answer: str
    question: str
    context: str
    explanation: str
    ratings: list[AnswerInfoRating]
    question_id: int
    question_name: str
    message_id: int
    database_id: int
    relevant_parts: list[AnswerInfoRelevantPart]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "AnswerInfoResponse":
        return cls(
            answer_id = data["answer_id"],
            answer = data["answer"],
            question = data["question"],
            context = data["context"],
            explanation = data["explanation"],
            ratings = [AnswerInfoRating.from_json(item) for item in data["ratings"]],
            question_id = data["question_id"],
            question_name = data["question_name"],
            message_id = data["message_id"],
            database_id = data["database_id"],
            relevant_parts = [AnswerInfoRelevantPart.from_json(item) for item in data["relevant_parts"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["answer_id"] = self.answer_id
        data["answer"] = self.answer
        data["question"] = self.question
        data["context"] = self.context
        data["explanation"] = self.explanation
        data["ratings"] = [AnswerInfoRating.to_json(item) for item in self.ratings]
        data["question_id"] = self.question_id
        data["question_name"] = self.question_name
        data["message_id"] = self.message_id
        data["database_id"] = self.database_id
        data["relevant_parts"] = [AnswerInfoRelevantPart.to_json(item) for item in self.relevant_parts]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'AnswerInfoResponse':
        return cls(
            answer_id=69,
            answer="Hi, its kayoc here 😉💅",
            question="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            context="The only thing your eyes haven't told me is your name 👀🤔",
            explanation="Just like a fine wine, you get better with age 🍷👵",
            ratings=[AnswerInfoRating.example(), AnswerInfoRating.example()],
            question_id=420,
            question_name="The only thing your eyes haven't told me is your name 👀🤔",
            message_id=69,
            database_id=420,
            relevant_parts=[AnswerInfoRelevantPart.example(), AnswerInfoRelevantPart.example(), AnswerInfoRelevantPart.example(), AnswerInfoRelevantPart.example(), AnswerInfoRelevantPart.example()],
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=False,
        )

@dataclass
class RateAnswerRequest:
    rating: Literal["down", "neutral", "up"]
    answer_id: int

    @classmethod
    def from_json(cls, data: dict) -> "RateAnswerRequest":
        return cls(
            rating = data["rating"],
            answer_id = data["answer_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["rating"] = self.rating
        data["answer_id"] = self.answer_id

        return data

    @classmethod
    def example(cls) -> 'RateAnswerRequest':
        return cls(
            rating="down",
            answer_id=69,
        )

@dataclass
class RateAnswerResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "RateAnswerResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'RateAnswerResponse':
        return cls(
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=False,
        )

@dataclass
class RatePartRequest:
    rating: Literal["relevant", "irrelevant", "neutral"]
    part_id: int

    @classmethod
    def from_json(cls, data: dict) -> "RatePartRequest":
        return cls(
            rating = data["rating"],
            part_id = data["part_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["rating"] = self.rating
        data["part_id"] = self.part_id

        return data

    @classmethod
    def example(cls) -> 'RatePartRequest':
        return cls(
            rating="irrelevant",
            part_id=69,
        )

@dataclass
class RatePartResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "RatePartResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'RatePartResponse':
        return cls(
            succes=False,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )

@dataclass
class AddItemRequest:
    filename: str
    filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"]
    database_name: str
    folder_id: Optional[int]

    @classmethod
    def from_json(cls, data: dict) -> "AddItemRequest":
        return cls(
            filename = data["filename"],
            filetype = data["filetype"],
            database_name = data["database_name"],
            folder_id = data["folder_id"] if "folder_id" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["filename"] = self.filename
        data["filetype"] = self.filetype
        data["database_name"] = self.database_name
        
        if self.folder_id is not None:
            data["folder_id"] = self.folder_id


        return data

    @classmethod
    def example(cls) -> 'AddItemRequest':
        return cls(
            filename="I'm not a photographer, but I can picture us together 📸👫",
            filetype="html",
            database_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            folder_id=666,
        )

@dataclass
class AddItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "AddItemResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'AddItemResponse':
        return cls(
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=False,
        )

@dataclass
class ScrapeConfig:
    allow_external_links: bool
    load_dynamic: bool
    timeout_seconds: int
    max_pages: Optional[int]

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeConfig":
        return cls(
            allow_external_links = data["allow_external_links"],
            load_dynamic = data["load_dynamic"],
            timeout_seconds = data["timeout_seconds"],
            max_pages = data["max_pages"] if "max_pages" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["allow_external_links"] = self.allow_external_links
        data["load_dynamic"] = self.load_dynamic
        data["timeout_seconds"] = self.timeout_seconds
        
        if self.max_pages is not None:
            data["max_pages"] = self.max_pages


        return data

    @classmethod
    def example(cls) -> 'ScrapeConfig':
        return cls(
            allow_external_links=True,
            load_dynamic=True,
            timeout_seconds=69,
            max_pages=None,
        )

@dataclass
class ScrapeRequest:
    urls: list[str]
    database_name: str
    scrape_config: Optional[ScrapeConfig]
    depths: Optional[list[int]]
    folder_path: Optional[list[str]]
    background: Optional[bool]

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeRequest":
        return cls(
            urls = data["urls"],
            database_name = data["database_name"],
            scrape_config = data["scrape_config"] if "scrape_config" in data else None,
            depths = data["depths"] if "depths" in data else None,
            folder_path = data["folder_path"] if "folder_path" in data else None,
            background = data["background"] if "background" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["urls"] = self.urls
        data["database_name"] = self.database_name
        
        if self.scrape_config is not None:
            data["scrape_config"] = self.scrape_config

        
        if self.depths is not None:
            data["depths"] = self.depths

        
        if self.folder_path is not None:
            data["folder_path"] = self.folder_path

        
        if self.background is not None:
            data["background"] = self.background


        return data

    @classmethod
    def example(cls) -> 'ScrapeRequest':
        return cls(
            urls=["Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵"],
            database_name="Wanna go out? No strings attached 🍆🍑",
            scrape_config=ScrapeConfig.example(),
            depths=[666, 69, 69, 666, 666],
            folder_path=["I'm not a photographer, but I can picture us together 📸👫", "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵", "You must be a magician, because whenever I look at you, everyone else disappears ✨🎩"],
            background=False,
        )

@dataclass
class ScrapeResponse:
    succes: bool
    message: str
    done: bool
    nitems: int
    nerror: int
    nskip: int
    nlink: int

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
            nitems = data["nitems"],
            nerror = data["nerror"],
            nskip = data["nskip"],
            nlink = data["nlink"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["nitems"] = self.nitems
        data["nerror"] = self.nerror
        data["nskip"] = self.nskip
        data["nlink"] = self.nlink

        return data

    @classmethod
    def example(cls) -> 'ScrapeResponse':
        return cls(
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
            nitems=69,
            nerror=420,
            nskip=420,
            nlink=420,
        )

@dataclass
class ScrapeUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeUpdateResponse":
        return cls(
            task = data["task"],
            total = data["total"] if "total" in data else None,
            count = data["count"] if "count" in data else None,
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["task"] = self.task
        
        if self.total is not None:
            data["total"] = self.total

        
        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'ScrapeUpdateResponse':
        return cls(
            task="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            total=None,
            count=None,
            succes=True,
            message="You've got character! ㍼🥴",
            done=True,
        )

@dataclass
class ScrapeInfoRequest:
    scrape_id: int

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeInfoRequest":
        return cls(
            scrape_id = data["scrape_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["scrape_id"] = self.scrape_id

        return data

    @classmethod
    def example(cls) -> 'ScrapeInfoRequest':
        return cls(
            scrape_id=666,
        )

@dataclass
class ScrapeDatabase:
    database_id: int
    name: str

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeDatabase":
        return cls(
            database_id = data["database_id"],
            name = data["name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_id"] = self.database_id
        data["name"] = self.name

        return data

    @classmethod
    def example(cls) -> 'ScrapeDatabase':
        return cls(
            database_id=420,
            name="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )

@dataclass
class ScrapeItem:
    url: str
    type: str
    name: str
    folder: Optional[str]
    item_id: int

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeItem":
        return cls(
            url = data["url"],
            type = data["type"],
            name = data["name"],
            folder = data["folder"] if "folder" in data else None,
            item_id = data["item_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["url"] = self.url
        data["type"] = self.type
        data["name"] = self.name
        
        if self.folder is not None:
            data["folder"] = self.folder

        data["item_id"] = self.item_id

        return data

    @classmethod
    def example(cls) -> 'ScrapeItem':
        return cls(
            url="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            type="Wanna go out? No strings attached 🍆🍑",
            name="You've got character! ㍼🥴",
            folder=None,
            item_id=666,
        )

@dataclass
class ScrapeInfoResponse:
    scrape_id: int
    created_at: DateTime
    database: ScrapeDatabase
    items: list[ScrapeItem]
    empty_pages: list[str]
    get_page_errors: list[str]
    items_not_added_to_storage: list[str]
    items_already_in_database: list[str]
    items_with_same_hash_already_in_database: list[str]
    items_added_to_database: list[str]
    link_database_add_fails: int
    number_of_links_between_pages: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "ScrapeInfoResponse":
        return cls(
            scrape_id = data["scrape_id"],
            created_at = DateTime.from_json(data['created_at']),
            database = ScrapeDatabase.from_json(data['database']),
            items = [ScrapeItem.from_json(item) for item in data["items"]],
            empty_pages = data["empty_pages"],
            get_page_errors = data["get_page_errors"],
            items_not_added_to_storage = data["items_not_added_to_storage"],
            items_already_in_database = data["items_already_in_database"],
            items_with_same_hash_already_in_database = data["items_with_same_hash_already_in_database"],
            items_added_to_database = data["items_added_to_database"],
            link_database_add_fails = data["link_database_add_fails"],
            number_of_links_between_pages = data["number_of_links_between_pages"],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["scrape_id"] = self.scrape_id
        data["created_at"] = self.created_at.to_json()
        data["database"] = self.database.to_json()
        data["items"] = [ScrapeItem.to_json(item) for item in self.items]
        data["empty_pages"] = self.empty_pages
        data["get_page_errors"] = self.get_page_errors
        data["items_not_added_to_storage"] = self.items_not_added_to_storage
        data["items_already_in_database"] = self.items_already_in_database
        data["items_with_same_hash_already_in_database"] = self.items_with_same_hash_already_in_database
        data["items_added_to_database"] = self.items_added_to_database
        data["link_database_add_fails"] = self.link_database_add_fails
        data["number_of_links_between_pages"] = self.number_of_links_between_pages
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'ScrapeInfoResponse':
        return cls(
            scrape_id=69,
            created_at=DateTime.example(),
            database=ScrapeDatabase.example(),
            items=[ScrapeItem.example(), ScrapeItem.example(), ScrapeItem.example(), ScrapeItem.example(), ScrapeItem.example(), ScrapeItem.example()],
            empty_pages=["You must be a magician, because whenever I look at you, everyone else disappears ✨🎩"],
            get_page_errors=["The only thing your eyes haven't told me is your name 👀🤔", "I'm not a photographer, but I can picture us together 📸👫", "Hi, its kayoc here 😉💅", "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵"],
            items_not_added_to_storage=["Just like a fine wine, you get better with age 🍷👵"],
            items_already_in_database=["Wanna go out? No strings attached 🍆🍑", "Wanna go out? No strings attached 🍆🍑", "The only thing your eyes haven't told me is your name 👀🤔", "Wanna go out? No strings attached 🍆🍑", "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫", "You must be a magician, because whenever I look at you, everyone else disappears ✨🎩"],
            items_with_same_hash_already_in_database=["I'm not a photographer, but I can picture us together 📸👫", "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫", "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵", "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫", "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵"],
            items_added_to_database=["Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵", "Are you a parking ticket? Because you've got FINE written all over you 🚗🎫", "The only thing your eyes haven't told me is your name 👀🤔", "Wanna go out? No strings attached 🍆🍑", "Wanna go out? No strings attached 🍆🍑", "Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵"],
            link_database_add_fails=666,
            number_of_links_between_pages=420,
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )

@dataclass
class ItemInfoRequest:
    item_id: int

    @classmethod
    def from_json(cls, data: dict) -> "ItemInfoRequest":
        return cls(
            item_id = data["item_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id

        return data

    @classmethod
    def example(cls) -> 'ItemInfoRequest':
        return cls(
            item_id=69,
        )

@dataclass
class ItemInfoFolder:
    name: str
    folder_id: int

    @classmethod
    def from_json(cls, data: dict) -> "ItemInfoFolder":
        return cls(
            name = data["name"],
            folder_id = data["folder_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["name"] = self.name
        data["folder_id"] = self.folder_id

        return data

    @classmethod
    def example(cls) -> 'ItemInfoFolder':
        return cls(
            name="I'm not a photographer, but I can picture us together 📸👫",
            folder_id=420,
        )

@dataclass
class ItemLink:
    name: str
    link_id: int

    @classmethod
    def from_json(cls, data: dict) -> "ItemLink":
        return cls(
            name = data["name"],
            link_id = data["link_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["name"] = self.name
        data["link_id"] = self.link_id

        return data

    @classmethod
    def example(cls) -> 'ItemLink':
        return cls(
            name="You've got character! ㍼🥴",
            link_id=69,
        )

@dataclass
class ItemInfoResponse:
    link_id: int
    name: str
    type: str
    folder: ItemInfoFolder
    url: Optional[str]
    outgoing_links: list[ItemLink]
    incoming_links: list[ItemLink]
    storage_name: Optional[str]
    created_at: DateTime
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "ItemInfoResponse":
        return cls(
            link_id = data["link_id"],
            name = data["name"],
            type = data["type"],
            folder = ItemInfoFolder.from_json(data['folder']),
            url = data["url"] if "url" in data else None,
            outgoing_links = [ItemLink.from_json(item) for item in data["outgoing_links"]],
            incoming_links = [ItemLink.from_json(item) for item in data["incoming_links"]],
            storage_name = data["storage_name"] if "storage_name" in data else None,
            created_at = DateTime.from_json(data['created_at']),
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["link_id"] = self.link_id
        data["name"] = self.name
        data["type"] = self.type
        data["folder"] = self.folder.to_json()
        
        if self.url is not None:
            data["url"] = self.url

        data["outgoing_links"] = [ItemLink.to_json(item) for item in self.outgoing_links]
        data["incoming_links"] = [ItemLink.to_json(item) for item in self.incoming_links]
        
        if self.storage_name is not None:
            data["storage_name"] = self.storage_name

        data["created_at"] = self.created_at.to_json()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'ItemInfoResponse':
        return cls(
            link_id=666,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            type="Hi, its kayoc here 😉💅",
            folder=ItemInfoFolder.example(),
            url="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            outgoing_links=[ItemLink.example(), ItemLink.example()],
            incoming_links=[ItemLink.example(), ItemLink.example(), ItemLink.example(), ItemLink.example(), ItemLink.example()],
            storage_name=None,
            created_at=DateTime.example(),
            succes=False,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=False,
        )

@dataclass
class DeleteItemRequest:
    item_id: int

    @classmethod
    def from_json(cls, data: dict) -> "DeleteItemRequest":
        return cls(
            item_id = data["item_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id

        return data

    @classmethod
    def example(cls) -> 'DeleteItemRequest':
        return cls(
            item_id=420,
        )

@dataclass
class DeleteItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DeleteItemResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DeleteItemResponse':
        return cls(
            succes=False,
            message="Hi, its kayoc here 😉💅",
            done=True,
        )

@dataclass
class RenameItemRequest:
    item_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict) -> "RenameItemRequest":
        return cls(
            item_id = data["item_id"],
            new_name = data["new_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> 'RenameItemRequest':
        return cls(
            item_id=69,
            new_name="Wanna go out? No strings attached 🍆🍑",
        )

@dataclass
class RenameItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "RenameItemResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'RenameItemResponse':
        return cls(
            succes=True,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class MoveItemRequest:
    item_id: int
    new_folder_id: int

    @classmethod
    def from_json(cls, data: dict) -> "MoveItemRequest":
        return cls(
            item_id = data["item_id"],
            new_folder_id = data["new_folder_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id
        data["new_folder_id"] = self.new_folder_id

        return data

    @classmethod
    def example(cls) -> 'MoveItemRequest':
        return cls(
            item_id=666,
            new_folder_id=666,
        )

@dataclass
class MoveItemResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "MoveItemResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'MoveItemResponse':
        return cls(
            succes=False,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=True,
        )

@dataclass
class DeleteFolderRequest:
    folder_name: str
    database_name: str

    @classmethod
    def from_json(cls, data: dict) -> "DeleteFolderRequest":
        return cls(
            folder_name = data["folder_name"],
            database_name = data["database_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_name"] = self.folder_name
        data["database_name"] = self.database_name

        return data

    @classmethod
    def example(cls) -> 'DeleteFolderRequest':
        return cls(
            folder_name="The only thing your eyes haven't told me is your name 👀🤔",
            database_name="You've got character! ㍼🥴",
        )

@dataclass
class DeleteFolderResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DeleteFolderResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DeleteFolderResponse':
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )

@dataclass
class RenameFolderRequest:
    folder_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict) -> "RenameFolderRequest":
        return cls(
            folder_id = data["folder_id"],
            new_name = data["new_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> 'RenameFolderRequest':
        return cls(
            folder_id=420,
            new_name="Just like a fine wine, you get better with age 🍷👵",
        )

@dataclass
class RenameFolderResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "RenameFolderResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'RenameFolderResponse':
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=False,
        )

@dataclass
class UpdateFolderDescriptionRequest:
    folder_id: int
    new_description: str

    @classmethod
    def from_json(cls, data: dict) -> "UpdateFolderDescriptionRequest":
        return cls(
            folder_id = data["folder_id"],
            new_description = data["new_description"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["new_description"] = self.new_description

        return data

    @classmethod
    def example(cls) -> 'UpdateFolderDescriptionRequest':
        return cls(
            folder_id=666,
            new_description="Wanna go out? No strings attached 🍆🍑",
        )

@dataclass
class UpdateFolderDescriptionResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UpdateFolderDescriptionResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UpdateFolderDescriptionResponse':
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class FolderInfoRequest:
    folder_id: int
    build_id: Optional[int]

    @classmethod
    def from_json(cls, data: dict) -> "FolderInfoRequest":
        return cls(
            folder_id = data["folder_id"],
            build_id = data["build_id"] if "build_id" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        
        if self.build_id is not None:
            data["build_id"] = self.build_id


        return data

    @classmethod
    def example(cls) -> 'FolderInfoRequest':
        return cls(
            folder_id=69,
            build_id=None,
        )

@dataclass
class FoldeInfoSubFolder:
    folder_id: int
    name: str
    description: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "FoldeInfoSubFolder":
        return cls(
            folder_id = data["folder_id"],
            name = data["name"],
            description = data["description"] if "description" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name
        
        if self.description is not None:
            data["description"] = self.description


        return data

    @classmethod
    def example(cls) -> 'FoldeInfoSubFolder':
        return cls(
            folder_id=420,
            name="Wanna go out? No strings attached 🍆🍑",
            description=None,
        )

@dataclass
class FolderItemInfo:
    item_id: int
    name: str
    type: str
    url: Optional[str]
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict) -> "FolderItemInfo":
        return cls(
            item_id = data["item_id"],
            name = data["name"],
            type = data["type"],
            url = data["url"] if "url" in data else None,
            created_at = DateTime.from_json(data['created_at']),
        )

    def to_json(self) -> dict:
        data = dict()
        data["item_id"] = self.item_id
        data["name"] = self.name
        data["type"] = self.type
        
        if self.url is not None:
            data["url"] = self.url

        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> 'FolderItemInfo':
        return cls(
            item_id=666,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            type="You've got character! ㍼🥴",
            url="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            created_at=DateTime.example(),
        )

@dataclass
class FolderInfoResponse:
    folder_id: int
    name: str
    description: Optional[str]
    created_at: DateTime
    subfolders: list[FoldeInfoSubFolder]
    items: list[FolderItemInfo]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "FolderInfoResponse":
        return cls(
            folder_id = data["folder_id"],
            name = data["name"],
            description = data["description"] if "description" in data else None,
            created_at = DateTime.from_json(data['created_at']),
            subfolders = [FoldeInfoSubFolder.from_json(item) for item in data["subfolders"]],
            items = [FolderItemInfo.from_json(item) for item in data["items"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name
        
        if self.description is not None:
            data["description"] = self.description

        data["created_at"] = self.created_at.to_json()
        data["subfolders"] = [FoldeInfoSubFolder.to_json(item) for item in self.subfolders]
        data["items"] = [FolderItemInfo.to_json(item) for item in self.items]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'FolderInfoResponse':
        return cls(
            folder_id=666,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            description=None,
            created_at=DateTime.example(),
            subfolders=[FoldeInfoSubFolder.example(), FoldeInfoSubFolder.example(), FoldeInfoSubFolder.example()],
            items=[FolderItemInfo.example(), FolderItemInfo.example(), FolderItemInfo.example(), FolderItemInfo.example(), FolderItemInfo.example(), FolderItemInfo.example()],
            succes=False,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )

@dataclass
class BuildConfig:
    datastore_type: Literal["chromastore", "vectorstore"]
    datastore_types: Optional[list[Literal["chromastore", "vectorstore"]]]

    @classmethod
    def from_json(cls, data: dict) -> "BuildConfig":
        return cls(
            datastore_type = data["datastore_type"],
            datastore_types = data["datastore_types"] if "datastore_types" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["datastore_type"] = self.datastore_type
        
        if self.datastore_types is not None:
            data["datastore_types"] = self.datastore_types


        return data

    @classmethod
    def example(cls) -> 'BuildConfig':
        return cls(
            datastore_type="vectorstore",
            datastore_types=None,
        )

@dataclass
class BuildRequest:
    database_name: str
    build_name: str
    build_config: Optional[BuildConfig]
    embed_config: Optional[EmbedConfig]
    background: Optional[bool]

    @classmethod
    def from_json(cls, data: dict) -> "BuildRequest":
        return cls(
            database_name = data["database_name"],
            build_name = data["build_name"],
            build_config = data["build_config"] if "build_config" in data else None,
            embed_config = data["embed_config"] if "embed_config" in data else None,
            background = data["background"] if "background" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name
        data["build_name"] = self.build_name
        
        if self.build_config is not None:
            data["build_config"] = self.build_config

        
        if self.embed_config is not None:
            data["embed_config"] = self.embed_config

        
        if self.background is not None:
            data["background"] = self.background


        return data

    @classmethod
    def example(cls) -> 'BuildRequest':
        return cls(
            database_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            build_name="I'm not a photographer, but I can picture us together 📸👫",
            build_config=BuildConfig.example(),
            embed_config=None,
            background=None,
        )

@dataclass
class BuildResponse:
    succes: bool
    message: str
    done: bool
    build_id: int
    nitems: Optional[int]
    nerror: Optional[int]

    @classmethod
    def from_json(cls, data: dict) -> "BuildResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
            build_id = data["build_id"],
            nitems = data["nitems"] if "nitems" in data else None,
            nerror = data["nerror"] if "nerror" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["build_id"] = self.build_id
        
        if self.nitems is not None:
            data["nitems"] = self.nitems

        
        if self.nerror is not None:
            data["nerror"] = self.nerror


        return data

    @classmethod
    def example(cls) -> 'BuildResponse':
        return cls(
            succes=False,
            message="Hi, its kayoc here 😉💅",
            done=False,
            build_id=666,
            nitems=None,
            nerror=666,
        )

@dataclass
class BuildUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "BuildUpdateResponse":
        return cls(
            task = data["task"],
            total = data["total"] if "total" in data else None,
            count = data["count"] if "count" in data else None,
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["task"] = self.task
        
        if self.total is not None:
            data["total"] = self.total

        
        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'BuildUpdateResponse':
        return cls(
            task="I'm not a photographer, but I can picture us together 📸👫",
            total=666,
            count=666,
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=False,
        )

@dataclass
class UpdateBuildRequest:
    database_name: str
    build_name: str
    background: Optional[bool]

    @classmethod
    def from_json(cls, data: dict) -> "UpdateBuildRequest":
        return cls(
            database_name = data["database_name"],
            build_name = data["build_name"],
            background = data["background"] if "background" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["database_name"] = self.database_name
        data["build_name"] = self.build_name
        
        if self.background is not None:
            data["background"] = self.background


        return data

    @classmethod
    def example(cls) -> 'UpdateBuildRequest':
        return cls(
            database_name="Wanna go out? No strings attached 🍆🍑",
            build_name="You've got character! ㍼🥴",
            background=False,
        )

@dataclass
class UpdateBuildResponse:
    succes: bool
    message: str
    done: bool
    build_id: int
    nitems: Optional[int]
    nerror: Optional[int]

    @classmethod
    def from_json(cls, data: dict) -> "UpdateBuildResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
            build_id = data["build_id"],
            nitems = data["nitems"] if "nitems" in data else None,
            nerror = data["nerror"] if "nerror" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done
        data["build_id"] = self.build_id
        
        if self.nitems is not None:
            data["nitems"] = self.nitems

        
        if self.nerror is not None:
            data["nerror"] = self.nerror


        return data

    @classmethod
    def example(cls) -> 'UpdateBuildResponse':
        return cls(
            succes=True,
            message="You've got character! ㍼🥴",
            done=False,
            build_id=666,
            nitems=None,
            nerror=None,
        )

@dataclass
class UpdateBuildUpdateResponse:
    task: str
    total: Optional[int]
    count: Optional[int]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UpdateBuildUpdateResponse":
        return cls(
            task = data["task"],
            total = data["total"] if "total" in data else None,
            count = data["count"] if "count" in data else None,
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["task"] = self.task
        
        if self.total is not None:
            data["total"] = self.total

        
        if self.count is not None:
            data["count"] = self.count

        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UpdateBuildUpdateResponse':
        return cls(
            task="Wanna go out? No strings attached 🍆🍑",
            total=666,
            count=666,
            succes=False,
            message="Wanna go out? No strings attached 🍆🍑",
            done=False,
        )

@dataclass
class RenameBuildRequest:
    build_id: int
    new_name: str

    @classmethod
    def from_json(cls, data: dict) -> "RenameBuildRequest":
        return cls(
            build_id = data["build_id"],
            new_name = data["new_name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["build_id"] = self.build_id
        data["new_name"] = self.new_name

        return data

    @classmethod
    def example(cls) -> 'RenameBuildRequest':
        return cls(
            build_id=69,
            new_name="Hi, its kayoc here 😉💅",
        )

@dataclass
class RenameBuildResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "RenameBuildResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'RenameBuildResponse':
        return cls(
            succes=True,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class DeleteBuildRequest:
    build_id: int

    @classmethod
    def from_json(cls, data: dict) -> "DeleteBuildRequest":
        return cls(
            build_id = data["build_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["build_id"] = self.build_id

        return data

    @classmethod
    def example(cls) -> 'DeleteBuildRequest':
        return cls(
            build_id=69,
        )

@dataclass
class DeleteBuildResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DeleteBuildResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DeleteBuildResponse':
        return cls(
            succes=False,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=True,
        )

@dataclass
class BuildInfoRequest:
    build_id: int

    @classmethod
    def from_json(cls, data: dict) -> "BuildInfoRequest":
        return cls(
            build_id = data["build_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["build_id"] = self.build_id

        return data

    @classmethod
    def example(cls) -> 'BuildInfoRequest':
        return cls(
            build_id=666,
        )

@dataclass
class BuildInfoQuestion:
    question_id: int
    first_message: str
    name: Optional[str]
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict) -> "BuildInfoQuestion":
        return cls(
            question_id = data["question_id"],
            first_message = data["first_message"],
            name = data["name"] if "name" in data else None,
            created_at = DateTime.from_json(data['created_at']),
        )

    def to_json(self) -> dict:
        data = dict()
        data["question_id"] = self.question_id
        data["first_message"] = self.first_message
        
        if self.name is not None:
            data["name"] = self.name

        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> 'BuildInfoQuestion':
        return cls(
            question_id=69,
            first_message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            name=None,
            created_at=DateTime.example(),
        )

@dataclass
class BuildInfoDatabaseFolder:
    folder_id: int
    name: str
    description: Optional[str]
    created_at: DateTime

    @classmethod
    def from_json(cls, data: dict) -> "BuildInfoDatabaseFolder":
        return cls(
            folder_id = data["folder_id"],
            name = data["name"],
            description = data["description"] if "description" in data else None,
            created_at = DateTime.from_json(data['created_at']),
        )

    def to_json(self) -> dict:
        data = dict()
        data["folder_id"] = self.folder_id
        data["name"] = self.name
        
        if self.description is not None:
            data["description"] = self.description

        data["created_at"] = self.created_at.to_json()

        return data

    @classmethod
    def example(cls) -> 'BuildInfoDatabaseFolder':
        return cls(
            folder_id=666,
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            description=None,
            created_at=DateTime.example(),
        )

@dataclass
class BuildInfoResponse:
    build_id: int
    name: str
    created_at: DateTime
    database_id: int
    question: list[BuildInfoQuestion]
    nitems: int
    database_folder: BuildInfoDatabaseFolder
    datastore_size_bytes: int
    size_bytes: int
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "BuildInfoResponse":
        return cls(
            build_id = data["build_id"],
            name = data["name"],
            created_at = DateTime.from_json(data['created_at']),
            database_id = data["database_id"],
            question = [BuildInfoQuestion.from_json(item) for item in data["question"]],
            nitems = data["nitems"],
            database_folder = BuildInfoDatabaseFolder.from_json(data['database_folder']),
            datastore_size_bytes = data["datastore_size_bytes"],
            size_bytes = data["size_bytes"],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["build_id"] = self.build_id
        data["name"] = self.name
        data["created_at"] = self.created_at.to_json()
        data["database_id"] = self.database_id
        data["question"] = [BuildInfoQuestion.to_json(item) for item in self.question]
        data["nitems"] = self.nitems
        data["database_folder"] = self.database_folder.to_json()
        data["datastore_size_bytes"] = self.datastore_size_bytes
        data["size_bytes"] = self.size_bytes
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'BuildInfoResponse':
        return cls(
            build_id=420,
            name="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            created_at=DateTime.example(),
            database_id=666,
            question=[BuildInfoQuestion.example()],
            nitems=666,
            database_folder=BuildInfoDatabaseFolder.example(),
            datastore_size_bytes=420,
            size_bytes=420,
            succes=True,
            message="I'm not a photographer, but I can picture us together 📸👫",
            done=False,
        )

@dataclass
class BuildListBuild:
    build_id: int
    build_name: str
    database_id: int
    database_name: str
    database_description: Optional[str]
    created_at: DateTime
    nitems: int
    datastore_size_bytes: int
    size_bytes: int

    @classmethod
    def from_json(cls, data: dict) -> "BuildListBuild":
        return cls(
            build_id = data["build_id"],
            build_name = data["build_name"],
            database_id = data["database_id"],
            database_name = data["database_name"],
            database_description = data["database_description"] if "database_description" in data else None,
            created_at = DateTime.from_json(data['created_at']),
            nitems = data["nitems"],
            datastore_size_bytes = data["datastore_size_bytes"],
            size_bytes = data["size_bytes"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["build_id"] = self.build_id
        data["build_name"] = self.build_name
        data["database_id"] = self.database_id
        data["database_name"] = self.database_name
        
        if self.database_description is not None:
            data["database_description"] = self.database_description

        data["created_at"] = self.created_at.to_json()
        data["nitems"] = self.nitems
        data["datastore_size_bytes"] = self.datastore_size_bytes
        data["size_bytes"] = self.size_bytes

        return data

    @classmethod
    def example(cls) -> 'BuildListBuild':
        return cls(
            build_id=69,
            build_name="I'm not a photographer, but I can picture us together 📸👫",
            database_id=420,
            database_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            database_description="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            created_at=DateTime.example(),
            nitems=666,
            datastore_size_bytes=666,
            size_bytes=69,
        )

@dataclass
class BuildListResponse:
    builds: list[BuildListBuild]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "BuildListResponse":
        return cls(
            builds = [BuildListBuild.from_json(item) for item in data["builds"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["builds"] = [BuildListBuild.to_json(item) for item in self.builds]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'BuildListResponse':
        return cls(
            builds=[BuildListBuild.example(), BuildListBuild.example(), BuildListBuild.example()],
            succes=True,
            message="You've got character! ㍼🥴",
            done=True,
        )

@dataclass
class CreateUserRequest:
    password: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    company: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "CreateUserRequest":
        return cls(
            password = data["password"],
            email = data["email"],
            first_name = data["first_name"] if "first_name" in data else None,
            last_name = data["last_name"] if "last_name" in data else None,
            company = data["company"] if "company" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["password"] = self.password
        data["email"] = self.email
        
        if self.first_name is not None:
            data["first_name"] = self.first_name

        
        if self.last_name is not None:
            data["last_name"] = self.last_name

        
        if self.company is not None:
            data["company"] = self.company


        return data

    @classmethod
    def example(cls) -> 'CreateUserRequest':
        return cls(
            password="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            email="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            first_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            last_name=None,
            company=None,
        )

@dataclass
class CreateUserResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "CreateUserResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'CreateUserResponse':
        return cls(
            succes=True,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class LoginRequest:
    email: str
    password: str

    @classmethod
    def from_json(cls, data: dict) -> "LoginRequest":
        return cls(
            email = data["email"],
            password = data["password"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["email"] = self.email
        data["password"] = self.password

        return data

    @classmethod
    def example(cls) -> 'LoginRequest':
        return cls(
            email="You've got character! ㍼🥴",
            password="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
        )

@dataclass
class LoginResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "LoginResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'LoginResponse':
        return cls(
            succes=False,
            message="Hi, its kayoc here 😉💅",
            done=True,
        )

@dataclass
class LogoutResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "LogoutResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'LogoutResponse':
        return cls(
            succes=True,
            message="The only thing your eyes haven't told me is your name 👀🤔",
            done=False,
        )

@dataclass
class OAuthRequest:
    provider: Literal["twitter", "google", "github", "facebook"]

    @classmethod
    def from_json(cls, data: dict) -> "OAuthRequest":
        return cls(
            provider = data["provider"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["provider"] = self.provider

        return data

    @classmethod
    def example(cls) -> 'OAuthRequest':
        return cls(
            provider="twitter",
        )

@dataclass
class OAuthResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "OAuthResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'OAuthResponse':
        return cls(
            succes=False,
            message="Roses are red, violets are blue, I'm not that pretty but damn look at you 🌹🔵",
            done=True,
        )

@dataclass
class OAuthAuthorizeRequest:
    provider: Literal["twitter", "google", "github", "facebook"]

    @classmethod
    def from_json(cls, data: dict) -> "OAuthAuthorizeRequest":
        return cls(
            provider = data["provider"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["provider"] = self.provider

        return data

    @classmethod
    def example(cls) -> 'OAuthAuthorizeRequest':
        return cls(
            provider="github",
        )

@dataclass
class OAuthAuthorizeResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "OAuthAuthorizeResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'OAuthAuthorizeResponse':
        return cls(
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=True,
        )

@dataclass
class BirthDay:
    day: int
    month: int
    year: int

    @classmethod
    def from_json(cls, data: dict) -> "BirthDay":
        return cls(
            day = data["day"],
            month = data["month"],
            year = data["year"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["day"] = self.day
        data["month"] = self.month
        data["year"] = self.year

        return data

    @classmethod
    def example(cls) -> 'BirthDay':
        return cls(
            day=666,
            month=420,
            year=69,
        )

@dataclass
class UpdateProfileRequest:
    first_name: Optional[str]
    last_name: Optional[str]
    company: Optional[str]
    birthday: Optional[BirthDay]

    @classmethod
    def from_json(cls, data: dict) -> "UpdateProfileRequest":
        return cls(
            first_name = data["first_name"] if "first_name" in data else None,
            last_name = data["last_name"] if "last_name" in data else None,
            company = data["company"] if "company" in data else None,
            birthday = data["birthday"] if "birthday" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        
        if self.first_name is not None:
            data["first_name"] = self.first_name

        
        if self.last_name is not None:
            data["last_name"] = self.last_name

        
        if self.company is not None:
            data["company"] = self.company

        
        if self.birthday is not None:
            data["birthday"] = self.birthday


        return data

    @classmethod
    def example(cls) -> 'UpdateProfileRequest':
        return cls(
            first_name=None,
            last_name=None,
            company="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            birthday=BirthDay.example(),
        )

@dataclass
class UpdateProfileResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UpdateProfileResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UpdateProfileResponse':
        return cls(
            succes=True,
            message="Wanna go out? No strings attached 🍆🍑",
            done=True,
        )

@dataclass
class UserProfile:
    first_name: Optional[str]
    last_name: Optional[str]
    birthday: Optional[BirthDay]
    company: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "UserProfile":
        return cls(
            first_name = data["first_name"] if "first_name" in data else None,
            last_name = data["last_name"] if "last_name" in data else None,
            birthday = data["birthday"] if "birthday" in data else None,
            company = data["company"] if "company" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        
        if self.first_name is not None:
            data["first_name"] = self.first_name

        
        if self.last_name is not None:
            data["last_name"] = self.last_name

        
        if self.birthday is not None:
            data["birthday"] = self.birthday

        
        if self.company is not None:
            data["company"] = self.company


        return data

    @classmethod
    def example(cls) -> 'UserProfile':
        return cls(
            first_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            last_name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            birthday=BirthDay.example(),
            company="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
        )

@dataclass
class UserDatabase:
    id: int
    name: str
    permission: Literal["read", "write", "delete", "admin", "owner"]

    @classmethod
    def from_json(cls, data: dict) -> "UserDatabase":
        return cls(
            id = data["id"],
            name = data["name"],
            permission = data["permission"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["id"] = self.id
        data["name"] = self.name
        data["permission"] = self.permission

        return data

    @classmethod
    def example(cls) -> 'UserDatabase':
        return cls(
            id=420,
            name="I'm not a photographer, but I can picture us together 📸👫",
            permission="read",
        )

@dataclass
class UserApiToken:
    id: int
    token: str
    name: str
    created_at: DateTime
    last_used_at: Optional[DateTime]

    @classmethod
    def from_json(cls, data: dict) -> "UserApiToken":
        return cls(
            id = data["id"],
            token = data["token"],
            name = data["name"],
            created_at = DateTime.from_json(data['created_at']),
            last_used_at = data["last_used_at"] if "last_used_at" in data else None,
        )

    def to_json(self) -> dict:
        data = dict()
        data["id"] = self.id
        data["token"] = self.token
        data["name"] = self.name
        data["created_at"] = self.created_at.to_json()
        
        if self.last_used_at is not None:
            data["last_used_at"] = self.last_used_at


        return data

    @classmethod
    def example(cls) -> 'UserApiToken':
        return cls(
            id=69,
            token="You've got character! ㍼🥴",
            name="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            created_at=DateTime.example(),
            last_used_at=DateTime.example(),
        )

@dataclass
class UserInfoResponse:
    id: int
    email: str
    created_at: DateTime
    profile: UserProfile
    databases: list[UserDatabase]
    tokens: list[UserApiToken]
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UserInfoResponse":
        return cls(
            id = data["id"],
            email = data["email"],
            created_at = DateTime.from_json(data['created_at']),
            profile = UserProfile.from_json(data['profile']),
            databases = [UserDatabase.from_json(item) for item in data["databases"]],
            tokens = [UserApiToken.from_json(item) for item in data["tokens"]],
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["id"] = self.id
        data["email"] = self.email
        data["created_at"] = self.created_at.to_json()
        data["profile"] = self.profile.to_json()
        data["databases"] = [UserDatabase.to_json(item) for item in self.databases]
        data["tokens"] = [UserApiToken.to_json(item) for item in self.tokens]
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UserInfoResponse':
        return cls(
            id=666,
            email="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            created_at=DateTime.example(),
            profile=UserProfile.example(),
            databases=[UserDatabase.example(), UserDatabase.example()],
            tokens=[UserApiToken.example()],
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=False,
        )

@dataclass
class UpdatePasswordRequest:
    new_password: str

    @classmethod
    def from_json(cls, data: dict) -> "UpdatePasswordRequest":
        return cls(
            new_password = data["new_password"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["new_password"] = self.new_password

        return data

    @classmethod
    def example(cls) -> 'UpdatePasswordRequest':
        return cls(
            new_password="Hi, its kayoc here 😉💅",
        )

@dataclass
class UpdatePasswordResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UpdatePasswordResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UpdatePasswordResponse':
        return cls(
            succes=True,
            message="You must be a magician, because whenever I look at you, everyone else disappears ✨🎩",
            done=True,
        )

@dataclass
class UpdateEmailRequest:
    new_email: str

    @classmethod
    def from_json(cls, data: dict) -> "UpdateEmailRequest":
        return cls(
            new_email = data["new_email"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["new_email"] = self.new_email

        return data

    @classmethod
    def example(cls) -> 'UpdateEmailRequest':
        return cls(
            new_email="You've got character! ㍼🥴",
        )

@dataclass
class UpdateEmailResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "UpdateEmailResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'UpdateEmailResponse':
        return cls(
            succes=False,
            message="You've got character! ㍼🥴",
            done=True,
        )

@dataclass
class DeleteUserResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DeleteUserResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DeleteUserResponse':
        return cls(
            succes=True,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=False,
        )

@dataclass
class CreateTokenRequest:
    name: str

    @classmethod
    def from_json(cls, data: dict) -> "CreateTokenRequest":
        return cls(
            name = data["name"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["name"] = self.name

        return data

    @classmethod
    def example(cls) -> 'CreateTokenRequest':
        return cls(
            name="Hi, its kayoc here 😉💅",
        )

@dataclass
class CreateTokenResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "CreateTokenResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'CreateTokenResponse':
        return cls(
            succes=False,
            message="Are you a parking ticket? Because you've got FINE written all over you 🚗🎫",
            done=False,
        )

@dataclass
class DeleteTokenRequest:
    token_id: int

    @classmethod
    def from_json(cls, data: dict) -> "DeleteTokenRequest":
        return cls(
            token_id = data["token_id"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["token_id"] = self.token_id

        return data

    @classmethod
    def example(cls) -> 'DeleteTokenRequest':
        return cls(
            token_id=666,
        )

@dataclass
class DeleteTokenResponse:
    succes: bool
    message: str
    done: bool

    @classmethod
    def from_json(cls, data: dict) -> "DeleteTokenResponse":
        return cls(
            succes = data["succes"],
            message = data["message"],
            done = data["done"],
        )

    def to_json(self) -> dict:
        data = dict()
        data["succes"] = self.succes
        data["message"] = self.message
        data["done"] = self.done

        return data

    @classmethod
    def example(cls) -> 'DeleteTokenResponse':
        return cls(
            succes=False,
            message="Wanna go out? No strings attached 🍆🍑",
            done=False,
        )
import requests
import aiohttp

import os
import json
from typing import Optional, Generator, AsyncGenerator, Union
import random
import asyncio


class KayocApi:

    def __init__(
        self,
        api_key: Optional[str] = None,
        session: Optional[requests.Session] = None,
        base_url: Optional[str] = None,
    ):
        self.session = requests.Session() if session is None else session
        self.base_url = "https://api.kayoc.nl" if base_url is None else base_url
        self.api_key = os.environ.get("None") if api_key is None else api_key

        if self.api_key is not None:
            self.session.headers.update({"Authorization": "Bearer " + self.api_key})

    def __repr__(self):
        return "{}({})".format(KayocApi, self.base_url)

    def __str__(self):
        return "{}({})".format(KayocApi, self.base_url)

    def close(self):
        self.session.close()

    def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/create"
            data = CreateDatabaseRequest(database_name=database_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return CreateDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/delete"
            data = DeleteDatabaseRequest(database_name=database_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_info(
        self, database_name: str
    ) -> Union[DatabaseInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/info"
            data = DatabaseInfoRequest(database_name=database_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_update_name(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/update/name"
            data = RenameDatabaseRequest(
                database_name=database_name, new_name=new_name
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_update_description(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/update/description"
            data = DatabaseUpdateDescriptionRequest(
                database_name=database_name, new_description=new_description
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseUpdateDescriptionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        try:
            url = self.base_url + "/database/browse"
            data = DatabaseBrowseRequest(
                fuzzy_database_name=fuzzy_database_name
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseBrowseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_update_permission(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        try:
            url = self.base_url + "/database/update/permission"
            data = DatabaseUpdatePermissionRequest(
                database_name=database_name,
                user_email=user_email,
                new_permission=new_permission,
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseUpdatePermissionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/publish"
            data = PublishDatabaseRequest(database_name=database_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return PublishDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/unpublish"
            data = UnpublishDatabaseRequest(database_name=database_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UnpublishDatabaseResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        try:
            url = self.base_url + "/database/list"
            data = None
            response = self.session.get(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DatabaseListResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/question/info"
            data = QuestionInfoRequest(question_id=question_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return QuestionInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        try:
            url = self.base_url + "/database/question/list"
            data = None
            response = self.session.get(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return QuestionListResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_question_update_name(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        try:
            url = self.base_url + "/database/question/update/name"
            data = UpdateQuestionNameRequest(
                question_id=question_id, new_name=new_name
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateQuestionNameResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_answer_create(
        self,
        question: str,
        database_name: str,
        question_id: Optional[int] = None,
        build_name: Optional[str] = None,
        keywords: Optional[list[str]] = None,
        top_k: Optional[int] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> Generator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None, None
    ]:
        url = self.base_url + "/database/answer/create"

        try:
            response = self.session.post(
                url,
                json=CreateAnswerRequest(
                    question=question,
                    database_name=database_name,
                    question_id=question_id,
                    build_name=build_name,
                    keywords=keywords,
                    top_k=top_k,
                    answer_config=answer_config,
                    retrieve_config=retrieve_config,
                    rerank_config=rerank_config,
                ).to_json(),
                stream=True,
            )

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield CreateAnswerResponse.from_json(update)
                    return
                else:
                    yield CreateAnswerUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def database_answer_info(
        self, answer_id: int
    ) -> Union[AnswerInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/answer/info"
            data = AnswerInfoRequest(answer_id=answer_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return AnswerInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        try:
            url = self.base_url + "/database/answer/rate"
            data = RateAnswerRequest(rating=rating, answer_id=answer_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RateAnswerResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_answer_part_rate(
        self, rating: Literal["relevant", "irrelevant", "neutral"], part_id: int
    ) -> Union[RatePartResponse, KayocError]:
        try:
            url = self.base_url + "/database/answer/part/rate"
            data = RatePartRequest(rating=rating, part_id=part_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RatePartResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/add"
            data = AddItemRequest(
                filename=filename,
                filetype=filetype,
                database_name=database_name,
                folder_id=folder_id,
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return AddItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_scrape(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None, None]:
        url = self.base_url + "/database/item/scrape"

        try:
            response = self.session.post(
                url,
                json=ScrapeRequest(
                    urls=urls,
                    database_name=database_name,
                    scrape_config=scrape_config,
                    depths=depths,
                    folder_path=folder_path,
                    background=background,
                ).to_json(),
                stream=True,
            )

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield ScrapeResponse.from_json(update)
                    return
                else:
                    yield ScrapeUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def database_item_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/scrape/info"
            data = ScrapeInfoRequest(scrape_id=scrape_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return ScrapeInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_info(self, item_id: int) -> Union[ItemInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/info"
            data = ItemInfoRequest(item_id=item_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return ItemInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_delete(
        self, item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/delete"
            data = DeleteItemRequest(item_id=item_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_update_name(
        self, item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/update/name"
            data = RenameItemRequest(item_id=item_id, new_name=new_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_move(
        self, item_id: int, new_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/move"
            data = MoveItemRequest(
                item_id=item_id, new_folder_id=new_folder_id
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return MoveItemResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_folder_delete(
        self, folder_name: str, database_name: str
    ) -> Union[DeleteFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/delete"
            data = DeleteFolderRequest(
                folder_name=folder_name, database_name=database_name
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteFolderResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_folder_update_name(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/update/name"
            data = RenameFolderRequest(folder_id=folder_id, new_name=new_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameFolderResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_folder_update_description(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/update/description"
            data = UpdateFolderDescriptionRequest(
                folder_id=folder_id, new_description=new_description
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateFolderDescriptionResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_item_folder_info(
        self, folder_id: int, build_id: Optional[int] = None
    ) -> Union[FolderInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/info"
            data = FolderInfoRequest(folder_id=folder_id, build_id=build_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return FolderInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_build_create(
        self,
        database_name: str,
        build_name: str,
        build_config: Optional[BuildConfig] = None,
        embed_config: Optional[EmbedConfig] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[BuildResponse, KayocError, BuildUpdateResponse], None, None]:
        url = self.base_url + "/database/build/create"

        try:
            response = self.session.post(
                url,
                json=BuildRequest(
                    database_name=database_name,
                    build_name=build_name,
                    build_config=build_config,
                    embed_config=embed_config,
                    background=background,
                ).to_json(),
                stream=True,
            )

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield BuildResponse.from_json(update)
                    return
                else:
                    yield BuildUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def database_build_update(
        self, database_name: str, build_name: str, background: Optional[bool] = None
    ) -> Generator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None, None
    ]:
        url = self.base_url + "/database/build/update"

        try:
            response = self.session.post(
                url,
                json=UpdateBuildRequest(
                    database_name=database_name,
                    build_name=build_name,
                    background=background,
                ).to_json(),
                stream=True,
            )

            if response.status_code == 401:
                yield KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )
                return

            if not response.ok:
                yield KayocError.from_json(response.json())
                return

            for update in response.iter_lines():
                update = json.loads(update)
                if update["done"]:
                    if not update["succes"]:
                        yield KayocError.from_json(update)
                    else:
                        yield UpdateBuildResponse.from_json(update)
                    return
                else:
                    yield UpdateBuildUpdateResponse.from_json(update)
        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

        yield KayocError(
            message="Server did not return a done message",
            succes=False,
            error="",
            done=True,
        )

    def database_build_update_name(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/update/name"
            data = RenameBuildRequest(build_id=build_id, new_name=new_name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return RenameBuildResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_build_delete(
        self, build_id: int
    ) -> Union[DeleteBuildResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/delete"
            data = DeleteBuildRequest(build_id=build_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteBuildResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_build_info(
        self, build_id: int
    ) -> Union[BuildInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/info"
            data = BuildInfoRequest(build_id=build_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return BuildInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def database_build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/list"
            data = None
            response = self.session.get(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return BuildListResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_create(
        self,
        password: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/create"
            data = CreateUserRequest(
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                company=company,
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return CreateUserResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_login(self, email: str, password: str) -> Union[LoginResponse, KayocError]:
        try:
            url = self.base_url + "/user/login"
            data = LoginRequest(email=email, password=password).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return LoginResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        try:
            url = self.base_url + "/user/logout"
            data = None
            response = self.session.get(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return LogoutResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/login"
            data = OAuthRequest(provider=provider).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return OAuthResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/authorize"
            data = OAuthAuthorizeRequest(provider=provider).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return OAuthAuthorizeResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        try:
            url = self.base_url + "/user/profile/update"
            data = UpdateProfileRequest(
                first_name=first_name,
                last_name=last_name,
                company=company,
                birthday=birthday,
            ).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateProfileResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        try:
            url = self.base_url + "/user/info"
            data = None
            response = self.session.get(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UserInfoResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        try:
            url = self.base_url + "/user/password/update"
            data = UpdatePasswordRequest(new_password=new_password).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdatePasswordResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        try:
            url = self.base_url + "/user/email/update"
            data = UpdateEmailRequest(new_email=new_email).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return UpdateEmailResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/delete"
            data = None
            response = self.session.get(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteUserResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_token_create(self, name: str) -> Union[CreateTokenResponse, KayocError]:
        try:
            url = self.base_url + "/user/token/create"
            data = CreateTokenRequest(name=name).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return CreateTokenResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    def user_token_delete(
        self, token_id: int
    ) -> Union[DeleteTokenResponse, KayocError]:
        try:
            url = self.base_url + "/user/token/delete"
            data = DeleteTokenRequest(token_id=token_id).to_json()
            response = self.session.post(url, json=data)

            if response.status_code == 401:
                return KayocError(
                    message="You are not logged in",
                    succes=False,
                    error="nli",
                    done=True,
                )

            if response.status_code // 100 != 2:
                return KayocError.from_json(response.json())

            return DeleteTokenResponse.from_json(response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )


class KayocApiAsync:

    def __init__(
        self,
        asession: aiohttp.ClientSession,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ):

        self.asession = asession
        self.base_url = "https://api.kayoc.nl" if base_url is None else base_url
        self.api_key = os.environ.get("None") if api_key is None else api_key

        # TODO: add api key header

        raise NotImplementedError(
            "The async client is not working as expected yet. Please use the sync client for now."
        )

    @classmethod
    async def new(
        cls,
        asession: Optional[aiohttp.ClientSession] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> "KayocApiAsync":
        if asession is None:
            asession = aiohttp.ClientSession()

        return KayocApiAsync(asession, api_key, base_url)

        raise NotImplementedError(
            "The async client is not working as expected yet. Please use the sync client for now."
        )

    def __repr__(self):
        return "{}({})".format(KayocApi, self.base_url)

    def __str__(self):
        return "{}({})".format(KayocApi, self.base_url)

    async def close(self):
        await self.asession.close()

    async def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/create"
            async with self.asession.post(
                url, json=CreateDatabaseRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return CreateDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/delete"
            async with self.asession.post(
                url, json=DeleteDatabaseRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_info(
        self, database_name: str
    ) -> Union[DatabaseInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/info"
            async with self.asession.post(
                url, json=DatabaseInfoRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_update_name(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/update/name"
            async with self.asession.post(
                url,
                json=RenameDatabaseRequest(
                    database_name=database_name, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_update_description(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/update/description"
            async with self.asession.post(
                url,
                json=DatabaseUpdateDescriptionRequest(
                    database_name=database_name, new_description=new_description
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseUpdateDescriptionResponse.from_json(
                    await response.json()
                )
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        try:
            url = self.base_url + "/database/browse"
            async with self.asession.post(
                url,
                json=DatabaseBrowseRequest(
                    fuzzy_database_name=fuzzy_database_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseBrowseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_update_permission(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        try:
            url = self.base_url + "/database/update/permission"
            async with self.asession.post(
                url,
                json=DatabaseUpdatePermissionRequest(
                    database_name=database_name,
                    user_email=user_email,
                    new_permission=new_permission,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseUpdatePermissionResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/publish"
            async with self.asession.post(
                url, json=PublishDatabaseRequest(database_name=database_name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return PublishDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        try:
            url = self.base_url + "/database/unpublish"
            async with self.asession.post(
                url,
                json=UnpublishDatabaseRequest(database_name=database_name).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UnpublishDatabaseResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        try:
            url = self.base_url + "/database/list"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DatabaseListResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/question/info"
            async with self.asession.post(
                url, json=QuestionInfoRequest(question_id=question_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return QuestionInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        try:
            url = self.base_url + "/database/question/list"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return QuestionListResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_question_update_name(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        try:
            url = self.base_url + "/database/question/update/name"
            async with self.asession.post(
                url,
                json=UpdateQuestionNameRequest(
                    question_id=question_id, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateQuestionNameResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_answer_create(
        self,
        question: str,
        database_name: str,
        question_id: Optional[int] = None,
        build_name: Optional[str] = None,
        keywords: Optional[list[str]] = None,
        top_k: Optional[int] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> AsyncGenerator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None
    ]:
        url = self.base_url + "/database/answer/create"
        try:
            async with self.asession.post(
                url,
                json=CreateAnswerRequest(
                    question=question,
                    database_name=database_name,
                    question_id=question_id,
                    build_name=build_name,
                    keywords=keywords,
                    top_k=top_k,
                    answer_config=answer_config,
                    retrieve_config=retrieve_config,
                    rerank_config=rerank_config,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield CreateAnswerResponse.from_json(update)
                            return
                        else:
                            yield CreateAnswerUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_answer_info(
        self, answer_id: int
    ) -> Union[AnswerInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/answer/info"
            async with self.asession.post(
                url, json=AnswerInfoRequest(answer_id=answer_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return AnswerInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        try:
            url = self.base_url + "/database/answer/rate"
            async with self.asession.post(
                url,
                json=RateAnswerRequest(rating=rating, answer_id=answer_id).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RateAnswerResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_answer_part_rate(
        self, rating: Literal["relevant", "irrelevant", "neutral"], part_id: int
    ) -> Union[RatePartResponse, KayocError]:
        try:
            url = self.base_url + "/database/answer/part/rate"
            async with self.asession.post(
                url, json=RatePartRequest(rating=rating, part_id=part_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RatePartResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/add"
            async with self.asession.post(
                url,
                json=AddItemRequest(
                    filename=filename,
                    filetype=filetype,
                    database_name=database_name,
                    folder_id=folder_id,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return AddItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_scrape(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None]:
        url = self.base_url + "/database/item/scrape"
        try:
            async with self.asession.post(
                url,
                json=ScrapeRequest(
                    urls=urls,
                    database_name=database_name,
                    scrape_config=scrape_config,
                    depths=depths,
                    folder_path=folder_path,
                    background=background,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield ScrapeResponse.from_json(update)
                            return
                        else:
                            yield ScrapeUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/scrape/info"
            async with self.asession.post(
                url, json=ScrapeInfoRequest(scrape_id=scrape_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return ScrapeInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_info(
        self, item_id: int
    ) -> Union[ItemInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/info"
            async with self.asession.post(
                url, json=ItemInfoRequest(item_id=item_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return ItemInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_delete(
        self, item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/delete"
            async with self.asession.post(
                url, json=DeleteItemRequest(item_id=item_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_update_name(
        self, item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/update/name"
            async with self.asession.post(
                url,
                json=RenameItemRequest(item_id=item_id, new_name=new_name).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_move(
        self, item_id: int, new_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/move"
            async with self.asession.post(
                url,
                json=MoveItemRequest(
                    item_id=item_id, new_folder_id=new_folder_id
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return MoveItemResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_folder_delete(
        self, folder_name: str, database_name: str
    ) -> Union[DeleteFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/delete"
            async with self.asession.post(
                url,
                json=DeleteFolderRequest(
                    folder_name=folder_name, database_name=database_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteFolderResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_folder_update_name(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/update/name"
            async with self.asession.post(
                url,
                json=RenameFolderRequest(
                    folder_id=folder_id, new_name=new_name
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameFolderResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_folder_update_description(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/update/description"
            async with self.asession.post(
                url,
                json=UpdateFolderDescriptionRequest(
                    folder_id=folder_id, new_description=new_description
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateFolderDescriptionResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_item_folder_info(
        self, folder_id: int, build_id: Optional[int] = None
    ) -> Union[FolderInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/item/folder/info"
            async with self.asession.post(
                url,
                json=FolderInfoRequest(
                    folder_id=folder_id, build_id=build_id
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return FolderInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_build_create(
        self,
        database_name: str,
        build_name: str,
        build_config: Optional[BuildConfig] = None,
        embed_config: Optional[EmbedConfig] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[BuildResponse, KayocError, BuildUpdateResponse], None]:
        url = self.base_url + "/database/build/create"
        try:
            async with self.asession.post(
                url,
                json=BuildRequest(
                    database_name=database_name,
                    build_name=build_name,
                    build_config=build_config,
                    embed_config=embed_config,
                    background=background,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield BuildResponse.from_json(update)
                            return
                        else:
                            yield BuildUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_build_update(
        self, database_name: str, build_name: str, background: Optional[bool] = None
    ) -> AsyncGenerator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None
    ]:
        url = self.base_url + "/database/build/update"
        try:
            async with self.asession.post(
                url,
                json=UpdateBuildRequest(
                    database_name=database_name,
                    build_name=build_name,
                    background=background,
                ).to_json(),
                headers={"Content-Type": "application/json"},
                stream=True,
            ) as response:

                if response.status == 401:
                    yield KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )
                    return

                if response.status // 100 != 2:
                    yield KayocError.from_json(await response.json())
                    return

                buffer = b""
                async for chunk in response.content.iter_any():
                    buffer += chunk
                    while b"\\n" in buffer:
                        line, buffer = buffer.split(b"\\n", 1)
                        update = json.loads(line)
                        if update["done"]:
                            if not update["succes"]:
                                yield KayocError.from_json(update)
                            else:
                                yield UpdateBuildResponse.from_json(update)
                            return
                        else:
                            yield UpdateBuildUpdateResponse.from_json(update)
                yield KayocError(
                    message="Server did not return a done message",
                    succes=False,
                    error="sdnrdm",
                    done=True,
                )

        except Exception as e:
            yield KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_build_update_name(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/update/name"
            async with self.asession.post(
                url,
                json=RenameBuildRequest(build_id=build_id, new_name=new_name).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return RenameBuildResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_build_delete(
        self, build_id: int
    ) -> Union[DeleteBuildResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/delete"
            async with self.asession.post(
                url, json=DeleteBuildRequest(build_id=build_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteBuildResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_build_info(
        self, build_id: int
    ) -> Union[BuildInfoResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/info"
            async with self.asession.post(
                url, json=BuildInfoRequest(build_id=build_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return BuildInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def database_build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        try:
            url = self.base_url + "/database/build/list"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return BuildListResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_create(
        self,
        password: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/create"
            async with self.asession.post(
                url,
                json=CreateUserRequest(
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    company=company,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return CreateUserResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_login(
        self, email: str, password: str
    ) -> Union[LoginResponse, KayocError]:
        try:
            url = self.base_url + "/user/login"
            async with self.asession.post(
                url, json=LoginRequest(email=email, password=password).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return LoginResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        try:
            url = self.base_url + "/user/logout"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return LogoutResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/login"
            async with self.asession.post(
                url, json=OAuthRequest(provider=provider).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return OAuthResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        try:
            url = self.base_url + "/user/oauth/authorize"
            async with self.asession.post(
                url, json=OAuthAuthorizeRequest(provider=provider).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return OAuthAuthorizeResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        try:
            url = self.base_url + "/user/profile/update"
            async with self.asession.post(
                url,
                json=UpdateProfileRequest(
                    first_name=first_name,
                    last_name=last_name,
                    company=company,
                    birthday=birthday,
                ).to_json(),
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateProfileResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        try:
            url = self.base_url + "/user/info"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UserInfoResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        try:
            url = self.base_url + "/user/password/update"
            async with self.asession.post(
                url, json=UpdatePasswordRequest(new_password=new_password).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdatePasswordResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        try:
            url = self.base_url + "/user/email/update"
            async with self.asession.post(
                url, json=UpdateEmailRequest(new_email=new_email).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return UpdateEmailResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        try:
            url = self.base_url + "/user/delete"
            async with self.asession.get(url, json=None) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteUserResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_token_create(
        self, name: str
    ) -> Union[CreateTokenResponse, KayocError]:
        try:
            url = self.base_url + "/user/token/create"
            async with self.asession.post(
                url, json=CreateTokenRequest(name=name).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return CreateTokenResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )

    async def user_token_delete(
        self, token_id: int
    ) -> Union[DeleteTokenResponse, KayocError]:
        try:
            url = self.base_url + "/user/token/delete"
            async with self.asession.post(
                url, json=DeleteTokenRequest(token_id=token_id).to_json()
            ) as response:

                if response.status == 401:
                    return KayocError(
                        message="You are not logged in",
                        succes=False,
                        error="nli",
                        done=True,
                    )

                if response.status // 100 != 2:
                    return KayocError.from_json(await response.json())

                return DeleteTokenResponse.from_json(await response.json())
        except Exception as e:
            return KayocError(
                message=f"An error was raised in the client: {e}",
                succes=False,
                error="sww",
                done=True,
            )


class ExampleKayocApi:

    def __init__(
        self,
        error_rate: float = 0.1,
        max_updates: int = 10,
        stream_error_rate: float = 0.05,
    ):
        self.error_rate = error_rate
        self.max_updates = max_updates
        self.stream_error_rate = stream_error_rate

    def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_info(
        self, database_name: str
    ) -> Union[DatabaseInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_update_name(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_update_description(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdateDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseBrowseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_update_permission(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdatePermissionResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = PublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UnpublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseListResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionListResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_question_update_name(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateQuestionNameResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_answer_create(
        self,
        question: str,
        database_name: str,
        question_id: Optional[int] = None,
        build_name: Optional[str] = None,
        keywords: Optional[list[str]] = None,
        top_k: Optional[int] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> Generator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None, None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = CreateAnswerUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = CreateAnswerResponse.example()
        response.done = True
        response.succes = True
        yield response

    def database_answer_info(
        self, answer_id: int
    ) -> Union[AnswerInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AnswerInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateAnswerResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_answer_part_rate(
        self, rating: Literal["relevant", "irrelevant", "neutral"], part_id: int
    ) -> Union[RatePartResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RatePartResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AddItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_scrape(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None, None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = ScrapeUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = ScrapeResponse.example()
        response.done = True
        response.succes = True
        yield response

    def database_item_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ScrapeInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_info(self, item_id: int) -> Union[ItemInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ItemInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_delete(
        self, item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_update_name(
        self, item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_move(
        self, item_id: int, new_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = MoveItemResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_folder_delete(
        self, folder_name: str, database_name: str
    ) -> Union[DeleteFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_folder_update_name(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_folder_update_description(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateFolderDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_item_folder_info(
        self, folder_id: int, build_id: Optional[int] = None
    ) -> Union[FolderInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = FolderInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_build_create(
        self,
        database_name: str,
        build_name: str,
        build_config: Optional[BuildConfig] = None,
        embed_config: Optional[EmbedConfig] = None,
        background: Optional[bool] = None,
    ) -> Generator[Union[BuildResponse, KayocError, BuildUpdateResponse], None, None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = BuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = BuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    def database_build_update(
        self, database_name: str, build_name: str, background: Optional[bool] = None
    ) -> Generator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None, None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = UpdateBuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = UpdateBuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    def database_build_update_name(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_build_delete(
        self, build_id: int
    ) -> Union[DeleteBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_build_info(
        self, build_id: int
    ) -> Union[BuildInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def database_build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildListResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_create(
        self,
        password: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateUserResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_login(self, email: str, password: str) -> Union[LoginResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LoginResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LogoutResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthAuthorizeResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateProfileResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UserInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdatePasswordResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateEmailResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteUserResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_token_create(self, name: str) -> Union[CreateTokenResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateTokenResponse.example()
        response.done = True
        response.succes = True
        return response

    def user_token_delete(
        self, token_id: int
    ) -> Union[DeleteTokenResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteTokenResponse.example()
        response.done = True
        response.succes = True
        return response


class ExampleKayocApiAsync:

    def __init__(
        self,
        error_rate: float = 0.1,
        max_updates: int = 10,
        stream_error_rate: float = 0.05,
    ):
        self.error_rate = error_rate
        self.max_updates = max_updates
        self.stream_error_rate = stream_error_rate

    async def database_create(
        self, database_name: str
    ) -> Union[CreateDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_delete(
        self, database_name: str
    ) -> Union[DeleteDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_info(
        self, database_name: str
    ) -> Union[DatabaseInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_update_name(
        self, database_name: str, new_name: str
    ) -> Union[RenameDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_update_description(
        self, database_name: str, new_description: str
    ) -> Union[DatabaseUpdateDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdateDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_browse(
        self, fuzzy_database_name: str
    ) -> Union[DatabaseBrowseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseBrowseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_update_permission(
        self,
        database_name: str,
        user_email: str,
        new_permission: Literal["read", "write", "delete", "admin", "owner"],
    ) -> Union[DatabaseUpdatePermissionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseUpdatePermissionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_publish(
        self, database_name: str
    ) -> Union[PublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = PublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_unpublish(
        self, database_name: str
    ) -> Union[UnpublishDatabaseResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UnpublishDatabaseResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_list(
        self,
    ) -> Union[DatabaseListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DatabaseListResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_question_info(
        self, question_id: int
    ) -> Union[QuestionInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_question_list(
        self,
    ) -> Union[QuestionListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = QuestionListResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_question_update_name(
        self, question_id: int, new_name: str
    ) -> Union[UpdateQuestionNameResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateQuestionNameResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_answer_create(
        self,
        question: str,
        database_name: str,
        question_id: Optional[int] = None,
        build_name: Optional[str] = None,
        keywords: Optional[list[str]] = None,
        top_k: Optional[int] = None,
        answer_config: Optional[AnswerConfig] = None,
        retrieve_config: Optional[RetrieveConfig] = None,
        rerank_config: Optional[RerankConfig] = None,
    ) -> AsyncGenerator[
        Union[CreateAnswerResponse, KayocError, CreateAnswerUpdateResponse], None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = CreateAnswerUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = CreateAnswerResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def database_answer_info(
        self, answer_id: int
    ) -> Union[AnswerInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AnswerInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_answer_rate(
        self, rating: Literal["down", "neutral", "up"], answer_id: int
    ) -> Union[RateAnswerResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RateAnswerResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_answer_part_rate(
        self, rating: Literal["relevant", "irrelevant", "neutral"], part_id: int
    ) -> Union[RatePartResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RatePartResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_add(
        self,
        filename: str,
        filetype: Literal["pdf", "html", "xml", "txt", "docx", "md"],
        database_name: str,
        folder_id: Optional[int] = None,
    ) -> Union[AddItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = AddItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_scrape(
        self,
        urls: list[str],
        database_name: str,
        scrape_config: Optional[ScrapeConfig] = None,
        depths: Optional[list[int]] = None,
        folder_path: Optional[list[str]] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[ScrapeResponse, KayocError, ScrapeUpdateResponse], None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = ScrapeUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = ScrapeResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def database_item_scrape_info(
        self, scrape_id: int
    ) -> Union[ScrapeInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ScrapeInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_info(
        self, item_id: int
    ) -> Union[ItemInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = ItemInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_delete(
        self, item_id: int
    ) -> Union[DeleteItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_update_name(
        self, item_id: int, new_name: str
    ) -> Union[RenameItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_move(
        self, item_id: int, new_folder_id: int
    ) -> Union[MoveItemResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = MoveItemResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_folder_delete(
        self, folder_name: str, database_name: str
    ) -> Union[DeleteFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_folder_update_name(
        self, folder_id: int, new_name: str
    ) -> Union[RenameFolderResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameFolderResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_folder_update_description(
        self, folder_id: int, new_description: str
    ) -> Union[UpdateFolderDescriptionResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateFolderDescriptionResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_item_folder_info(
        self, folder_id: int, build_id: Optional[int] = None
    ) -> Union[FolderInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = FolderInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_build_create(
        self,
        database_name: str,
        build_name: str,
        build_config: Optional[BuildConfig] = None,
        embed_config: Optional[EmbedConfig] = None,
        background: Optional[bool] = None,
    ) -> AsyncGenerator[Union[BuildResponse, KayocError, BuildUpdateResponse], None]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = BuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = BuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def database_build_update(
        self, database_name: str, build_name: str, background: Optional[bool] = None
    ) -> AsyncGenerator[
        Union[UpdateBuildResponse, KayocError, UpdateBuildUpdateResponse], None
    ]:
        for _ in range(random.randint(1, self.max_updates)):
            if random.random() < self.stream_error_rate:
                error = KayocError.example()
                error.error = "re"
                error.done = True
                error.succes = False
                yield error
                return

            update = UpdateBuildUpdateResponse.example()
            update.done = False
            update.succes = True
            yield update

        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            yield error
            return

        response = UpdateBuildResponse.example()
        response.done = True
        response.succes = True
        yield response

    async def database_build_update_name(
        self, build_id: int, new_name: str
    ) -> Union[RenameBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = RenameBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_build_delete(
        self, build_id: int
    ) -> Union[DeleteBuildResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteBuildResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_build_info(
        self, build_id: int
    ) -> Union[BuildInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def database_build_list(
        self,
    ) -> Union[BuildListResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = BuildListResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_create(
        self,
        password: str,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Union[CreateUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateUserResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_login(
        self, email: str, password: str
    ) -> Union[LoginResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LoginResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_logout(
        self,
    ) -> Union[LogoutResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = LogoutResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_oauth_login(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_oauth_authorize(
        self, provider: Literal["twitter", "google", "github", "facebook"]
    ) -> Union[OAuthAuthorizeResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = OAuthAuthorizeResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_profile_update(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        birthday: Optional[BirthDay] = None,
    ) -> Union[UpdateProfileResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateProfileResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_info(
        self,
    ) -> Union[UserInfoResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UserInfoResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_password_update(
        self, new_password: str
    ) -> Union[UpdatePasswordResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdatePasswordResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_email_update(
        self, new_email: str
    ) -> Union[UpdateEmailResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = UpdateEmailResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_delete(
        self,
    ) -> Union[DeleteUserResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteUserResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_token_create(
        self, name: str
    ) -> Union[CreateTokenResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = CreateTokenResponse.example()
        response.done = True
        response.succes = True
        return response

    async def user_token_delete(
        self, token_id: int
    ) -> Union[DeleteTokenResponse, KayocError]:
        if random.random() < self.error_rate:
            error = KayocError.example()
            error.error = "re"
            error.done = True
            error.succes = False
            return error

        response = DeleteTokenResponse.example()
        response.done = True
        response.succes = True
        return response
