from typing import Optional, Dict, List
from TableauConMan.assets_manager import AssetsManager
from TableauConMan.helpers import utils
import tableauserverclient as TSC
from loguru import logger


class UserManager(AssetsManager):
    def __init__(self, plan) -> None:
        """

        :param plan:
        """
        AssetsManager.__init__(self, plan)
        self.target_groups: Optional[list[TSC.GroupItem]] = None
        self.target_groups_list: Optional[list] = None
        self.target_group_memberships_list: Optional[list] = None
        self.reference_groups: Optional[list[TSC.GroupItem]] = None
        self.reference_groups_list: Optional[list] = None
        self.reference_group_memberships_list: Optional[list] = None
        self.target_users: Optional[list] = None
        self.reference_users: Optional[list] = None

    def populate_server_users(self) -> Dict:
        """

        :return:
        """
        logger.info("Retrieving server users")
        with self.plan.target.connect():
            clean_dict = {
                user.email: user.site_role
                for user in TSC.Pager(self.plan.target.server.users)
            }
        logger.success("Server users retrieved")
        return clean_dict

    def create_user(self, user_name: str, role: str):
        """

        :param user_name:
        :param role:
        :return:
        """
        logger.info(f"Creating user: {user_name}, role: {role}")
        new_user = TSC.UserItem(user_name, role, auth_setting="SAML")

        with self.plan.target.connect():
            new_u = self.plan.target.server.users.add(new_user)
            logger.success("User added successfully")
            return new_u.id

    def delete_user(self, user_name: str) -> bool:
        """

        :param user_name:
        :return:
        """

        delete_user = self.get_user_by_name(user_name)

        logger.info(f"Deleting {user_name}")
        with self.plan.target.connect():
            self.plan.target.server.users.remove(delete_user.id)

        logger.success("Deleted user")
        return True

    def update_user(self, user_name: str, role: str) -> bool:
        """

        :param user_name:
        :param role:
        :return:
        """
        logger.info(f"Updating user: {user_name}")
        update_user = self.get_user_by_name(user_name)

        update_user.site_role = role

        with self.plan.target.connect():
            self.plan.target.server.users.update(update_user)

        logger.success("User updated")
        return True

    def get_user_by_name(self, user_name: str) -> TSC.UserItem:
        """

        :param user_name:
        :return:
        """
        # Sets up the request param to filter for the correct username.
        req_option = TSC.RequestOptions()
        req_option.filter.add(
            TSC.Filter(
                TSC.RequestOptions.Field.Name,
                TSC.RequestOptions.Operator.Equals,
                user_name,
            )
        )
        with self.plan.target.connect():
            all_users, pagination_item = self.plan.target.server.users.get(
                req_options=req_option
            )

            if pagination_item.total_available > 1:
                raise ValueError(
                    f"Multiple user names have been returned, {pagination_item.total_available}."
                )

            if pagination_item.total_available < 1:
                logger.warning(
                    f"No user was found matching the user name {user_name} on the site."
                )
                return

            return all_users[0]

    def compare_dicts(self, reference: Dict, target: Dict) -> [List, List, Dict]:
        """

        :param reference:
        :param target:
        :return:
        """
        keys_only_in_reference = [key for key in reference if key not in target]
        keys_only_in_target = [key for key in target if key not in reference]
        keys_with_different_values = [
            (key, reference[key])
            for key in reference
            if key in target and reference[key] != target[key]
        ]

        return keys_only_in_reference, keys_only_in_target, keys_with_different_values
