from dotenv import load_dotenv
from logger_local.Logger import Logger
from .organizations_constants import ORGANIZATIONS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT
from user_context_remote.user_context import UserContext
from database_mysql_local.generic_crud_ml import GenericCRUDML
from language_remote.lang_code import LangCode
from database_infrastructure_local.number_generator import NumberGenerator
load_dotenv()

logger = Logger(object=ORGANIZATIONS_PYTHON_PACKAGE_CODE_LOGGER_OBJECT)
user_context = UserContext()

DEFAULT_SCHEMA_NAME = "organization"
DEFAULT_TABLE_NAME = "organization_table"
DEFAULT_VIEW_NAME = "organization_view"
DEFAULT_ID_COLUMN_NAME = "organization_id"
DEFAULT_ML_TABLE_NAME = "organization_ml_table"
DEFAULT_ML_VIEW_NAME = "organization_ml_view"
DEFAULT_ML_ID_COLUMN_NAME = "organization_ml_id"
DEFAULT_NOT_DELETED_ML_VIEW_NAME = "organization_ml_not_deleted_view"

'''
"organization_table fields":
    "number",
    "identifier",
    "is_approved",
    "is_main",
    "point",
    "location_id",
    "profile_id",
    "parent_organization_id",
    "non_members_visibility_scope_id",
    "members_visibility_scope_id",
    "Non_members_visibility_profile_id",
    "is_test_data",
    "created_timestamp",
    "created_user_id",
    "created_real_user_id",
    "created_effective_user_id",
    "created_effective_profile_id",
    "updated_timestamp",
    "updated_user_id",
    "updated_real_user_id",
    "updated_effective_user_id",
    "updated_effective_profile_id",
    "start_timestamp",
    "end_timestamp",
    "main_group_id"

organization_ml_table fields:
    "organization_ml_id",
    "organization_id",
    "lang_code",
    "is_main",
    "name",
    "is_name_approved",
    "is_description_approved",
    "description"
'''


class OrganizationsLocal(GenericCRUDML):
    def __init__(self, default_schema_name=DEFAULT_SCHEMA_NAME, default_table_name=DEFAULT_TABLE_NAME,
                 default_id_column_name=DEFAULT_ID_COLUMN_NAME, is_test_data=False):
        GenericCRUDML.__init__(self, default_schema_name=default_schema_name,
                               default_table_name=default_table_name,
                               default_id_column_name=default_id_column_name,
                               is_test_data=is_test_data)
        self.default_view_table_name = DEFAULT_VIEW_NAME

    def add_value(self, organization_ml_data_json: dict, organization_data_json: dict = None,
                  table_name: str = None, ml_table_name: str = None, is_main: int = 0,
                  table_id: int = None, lang_code: LangCode = None) -> tuple[int, int]:
        logger.start(object={"organization_data_json": organization_data_json,
                             "organization_ml_data_json": organization_ml_data_json})
        table_name = table_name or self.default_table_name
        ml_table_name = ml_table_name or self.default_ml_table_name
        organization_data_json = organization_data_json or {}
        organization_id, organization_ml_id = GenericCRUDML.add_value(
            self,
            data_ml_json=organization_ml_data_json,
            table_id=table_id,
            lang_code=lang_code,
            is_main=is_main,
            data_json=organization_data_json,
            table_name=table_name,
            ml_table_name=ml_table_name
        )
        logger.end(object={"organization_id": organization_id,
                   "organization_ml_id": organization_ml_id})
        return organization_id, organization_ml_id

    def insert_organization(self, organization_dict: dict) -> tuple[int, int]:
        logger.start(object={'data': str(organization_dict)})
        number = NumberGenerator.get_random_number(
            schema_name=DEFAULT_SCHEMA_NAME, view_name=DEFAULT_VIEW_NAME)
        identifier = NumberGenerator.get_random_identifier(
            schema_name=DEFAULT_SCHEMA_NAME, view_name=DEFAULT_VIEW_NAME,
            identifier_column_name="identifier")
        organization_data_json = {
            "number": number,
            "identifier": identifier,
            "name": organization_dict.get('name'),
            "is_approved": organization_dict.get('is_approved'),
            "is_main": organization_dict.get('is_main'),
            "point": organization_dict.get('point'),
            "location_id": organization_dict.get('location_id'),
            "profile_id": organization_dict.get('profile_id'),
            "parent_organization_id": organization_dict.get('parent_organization_id'),
            "non_members_visibility_scope_id": organization_dict.get('non_members_visibility_scope_id'),
            "members_visibility_scope_id": organization_dict.get('members_visibility_scope_id'),
            "Non_members_visibility_profile_id": organization_dict.get('Non_members_visibility_profile_id'),
            "main_group_id": organization_dict.get('main_group_id')
        }
        organization_id = GenericCRUDML.insert(self, data_json=organization_data_json)

        organization_ml_data_json = {
            "organization_id": organization_id,
            "lang_code": organization_dict.get('lang_code'),
            "is_main": organization_dict.get('is_main'),
            "title": organization_dict.get('title'),
            "is_name_approved": organization_dict.get('is_name_approved'),
            "is_description_approved": organization_dict.get('is_description_approved'),
            "description": organization_dict.get('description')
        }
        organization_ml_id = GenericCRUDML.insert(self, table_name="organization_ml_table",
                                                  data_json=organization_ml_data_json)

        logger.end(object={'organization_id': organization_id,
                   'organization_ml_id': organization_ml_id})
        return organization_id, organization_ml_id

    def upsert_organization(self, organization_dict: dict, order_by: str = "") -> tuple[int, int]:
        logger.start(object={'data': str(organization_dict)})
        organization_id = self.select_one_value_by_where(
            view_table_name="organization_ml_view",
            select_clause_value="organization_id",
            where="title = %s AND lang_code = %s",
            params=(organization_dict.get('name'), organization_dict.get('lang_code')),
            order_by=order_by
        )
        organization_data_json_compare = None
        organization_ml_data_json_compare = None
        if organization_id:
            organization_data_json_compare = {
                "organization_id": organization_id,
            }
            organization_ml_data_json_compare = {
                "organization_id": organization_id,
                "lang_code": organization_dict.get('lang_code')
            }
        number = NumberGenerator.get_random_number(
            schema_name=DEFAULT_SCHEMA_NAME, view_name=DEFAULT_VIEW_NAME)
        identifier = NumberGenerator.get_random_identifier(
            schema_name=DEFAULT_SCHEMA_NAME, view_name=DEFAULT_VIEW_NAME,
            identifier_column_name="identifier")
        organization_data_json = {
            "number": number,   # TODO: if upsert updates then it changes this though it is not supposed to
            "identifier": identifier,   # TODO: if upsert updates then it changes this though it is not supposed to
            "name": organization_dict.get('name'),
            "is_approved": organization_dict.get('is_approved'),
            "is_main": organization_dict.get('is_main'),
            "point": organization_dict.get('point'),
            "location_id": organization_dict.get('location_id'),
            "profile_id": organization_dict.get('profile_id'),
            "parent_organization_id": organization_dict.get('parent_organization_id'),
            "non_members_visibility_scope_id": organization_dict.get('non_members_visibility_scope_id'),
            "members_visibility_scope_id": organization_dict.get('members_visibility_scope_id'),
            "Non_members_visibility_profile_id": organization_dict.get('Non_members_visibility_profile_id'),
            "main_group_id": organization_dict.get('main_group_id')
        }
        organization_id = GenericCRUDML.upsert(self, view_table_name=DEFAULT_NOT_DELETED_ML_VIEW_NAME,
                                               data_json=organization_data_json,
                                               data_json_compare=organization_data_json_compare,
                                               order_by=order_by)

        organization_ml_data_json = {
            "organization_id": organization_id,
            "lang_code": organization_dict.get('lang_code'),
            "is_main": organization_dict.get('is_main'),
            "title": organization_dict.get('title'),
            "is_name_approved": organization_dict.get('is_name_approved'),
            "is_description_approved": organization_dict.get('is_description_approved'),
            "description": organization_dict.get('description')
        }
        organization_ml_id = GenericCRUDML.upsert(self, table_name="organization_ml_table",
                                                  view_table_name=DEFAULT_NOT_DELETED_ML_VIEW_NAME,
                                                  data_json=organization_ml_data_json,
                                                  data_json_compare=organization_ml_data_json_compare,
                                                  order_by=order_by)

        logger.end(object={'organization_id': organization_id,
                   'organization_ml_id': organization_ml_id})
        return organization_id, organization_ml_id

    def update_organization(self, organization_id: int, organization_ml_id: int, organization_dict: dict) -> None:
        logger.start(object={'organization_id': organization_id, 'data': str(organization_dict)})
        number = NumberGenerator.get_random_number(
            schema_name=DEFAULT_SCHEMA_NAME, view_name=DEFAULT_VIEW_NAME)
        identifier = NumberGenerator.get_random_identifier(
            schema_name=DEFAULT_SCHEMA_NAME, view_name=DEFAULT_VIEW_NAME,
            identifier_column_name="identifier")
        organization_data_json = {
            "number": number,
            "identifier": identifier,
            "name": organization_dict.get('name'),
            "is_approved": organization_dict.get('is_approved'),
            "is_main": organization_dict.get('is_main'),
            "point": organization_dict.get('point'),
            "location_id": organization_dict.get('location_id'),
            "profile_id": organization_dict.get('profile_id'),
            "parent_organization_id": organization_dict.get('parent_organization_id'),
            "non_members_visibility_scope_id": organization_dict.get('non_members_visibility_scope_id'),
            "members_visibility_scope_id": organization_dict.get('members_visibility_scope_id'),
            "Non_members_visibility_profile_id": organization_dict.get('Non_members_visibility_profile_id'),
            "main_group_id": organization_dict.get('main_group_id')
        }
        GenericCRUDML.update_by_id(self, id_column_value=organization_id,
                                   data_json=organization_data_json)

        organization_ml_data_json = {
            "organization_id": organization_id,
            "lang_code": organization_dict.get('lang_code'),
            "is_main": organization_dict.get('is_main'),
            "title": organization_dict.get('title'),
            "is_name_approved": organization_dict.get('is_name_approved'),
            "is_description_approved": organization_dict.get('is_description_approved'),
            "description": organization_dict.get('description')
        }
        GenericCRUDML.update_by_id(self, table_name="organization_ml_table",
                                   id_column_value=organization_ml_id, data_json=organization_ml_data_json,
                                   id_column_name="organization_ml_id")
        logger.end()

    def get_organization_dict_by_organization_id(self, organization_id: int, organization_ml_id: int = None,
                                                 view_table_name: str = None) -> dict:
        logger.start(object={'organization_id': organization_id})
        view_table_name = view_table_name or self.default_view_table_name
        organization_ml_dict = {}
        if organization_ml_id:
            organization_ml_dict = self.select_one_dict_by_id(view_table_name="organization_ml_view",
                                                              id_column_value=organization_ml_id,
                                                              id_column_name="organization_ml_id")
        organization_dict = self.select_one_dict_by_id(view_table_name=view_table_name, id_column_value=organization_id,
                                                       id_column_name="organization_id")
        logger.end(object={'organization_ml_dict': str(organization_ml_dict)})
        return {**organization_dict, **organization_ml_dict}

    def delete_by_organization_id(self, organization_id: int, organization_ml_id: int = None) -> None:
        logger.start(object={'organization_id': organization_id})
        # Delete from organization_table
        self.delete_by_id(table_name="organization_table",
                          id_column_name="organization_id", id_column_value=organization_id)
        # Delete from organization_ml_table
        if organization_ml_id:
            self.delete_by_id(table_name="organization_ml_table", id_column_name="organization_ml_id",
                              id_column_value=organization_ml_id)
        logger.end()

    def get_test_organization_id(self) -> int:
        return self.get_test_entity_id(
            entity_name="organization",
            insert_function=self.insert_organization
        )
