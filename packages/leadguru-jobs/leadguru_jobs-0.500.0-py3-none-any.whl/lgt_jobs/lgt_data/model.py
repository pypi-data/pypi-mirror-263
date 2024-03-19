from __future__ import annotations
import copy
import json
from abc import ABC
from datetime import datetime, UTC
from typing import Optional, List, Dict
from .enums import UserRole, SourceType, FeaturesEnum, FeatureOptions
from .helpers import get_linkedin_search_contact
from bson import ObjectId


class DictionaryModel(ABC):
    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        if '_id' in dic:
            setattr(model, 'id', dic['_id'])

        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        return result


class BaseModel(DictionaryModel):
    def __init__(self):
        self.id = None
        self.created_at = datetime.now(UTC)


class Credentials(BaseModel):
    def __init__(self):
        super().__init__()
        self.token = None
        self.cookies = None
        self.invalid_creds = False


class Source:
    def __init__(self):
        self.source_type: SourceType | None = None
        self.source_name = None
        self.source_id = None

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        return result


class BaseConfig:
    def __init__(self):
        self.owner = None
        self.id = None

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        return result


class Config(BaseConfig):
    def __init__(self):
        super().__init__()
        self.name = None


class BaseBotModel(Credentials):
    def __init__(self):
        super().__init__()
        self.created_by = None
        self.user_name = None
        self.slack_url = None
        self.registration_link = None
        self.channels = None
        self.connected_channels = None
        self.channels_users = None
        self.users_count = None
        self.messages_received: int = 0
        self.messages_filtered: int = 0
        self.recent_messages: List[str] = []
        self.icon = None
        self.active_channels = {}
        self.paused_channels = []
        self.source: Source | None = None
        self.two_factor_required: bool = False
        self.banned: bool = False
        self.associated_user = None
        self.type: SourceType | None = None
        self.deleted = False


class DedicatedBotModel(BaseBotModel):
    def __init__(self):
        super().__init__()
        self.user_id: Optional[str] = None
        self.updated_at: Optional[datetime] = datetime.now(UTC)
        self.servers: List[Server] = []
        self.state = 0
        self.source: Source | None = None

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)

        if result.get('source'):
            result['source'] = Source.to_dic(result.get('source'))

        result['servers'] = [Server.to_dic(server) for server in self.servers]
        return result

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model: DedicatedBotModel = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        if '_id' in dic:
            setattr(model, 'id', dic['_id'])

        model.source = Source.from_dic(dic.get("source"))
        model.servers = [Server.from_dic(server) for server in dic.get("servers", [])]
        return model


class Server:
    pass

    def __init__(self):
        self.id = None
        self.name = None
        self.channels: List[Channel] = []
        self.icon = None
        self.active = False
        self.deleted = False
        self.subscribers = 0

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            if hasattr(model, k):
                setattr(model, k, v)

        model.channels = [Channel.from_dic(channel) for channel in dic.get("channels", [])]
        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        result['channels'] = [Channel.to_dic(channel) for channel in self.channels]
        return result


class Channel:
    pass

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.is_member = True
        self.active = True
        self.subscribers = 0

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            if hasattr(model, k):
                setattr(model, k, v)

        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        return result


class MessageModel:
    pass

    def __init__(self):
        self.message_id = None
        self.channel_id = None
        self.channel_name = None
        self.message = None
        self.name = None
        self.sender_id = None
        self.source: Source | None = None
        self.companies: List[str] = list()
        self.technologies: List[str] = list()
        self.locations: List[str] = list()
        self.configs: List[BaseConfig] = list()
        self.attachments: List[dict] = []
        self.timestamp = None
        self.tags: List[str] = []

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None
        if isinstance(dic.get('attachments'), str):
            dic['attachments'] = json.loads(dic['attachments'])

        model: MessageModel = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        model.source = Source.from_dic(dic.get("source"))
        model.configs = [BaseConfig.from_dic(doc) for doc in dic.get("configs", [])]
        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)

        if result.get('source'):
            result['source'] = Source.to_dic(result.get('source'))
        if result.get('configs'):
            result['configs'] = [BaseConfig.to_dic(config) for config in result.get('configs')]
        return result


class UserModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.email: Optional[str] = None
        self.password: Optional[str] = None
        self.roles: List[str] = []
        self.user_name: str = ''
        self.company: str = ''
        self.company_size: Optional[int] = None
        self.company_industries: Optional[List[str]] = None
        self.company_technologies: Optional[List[str]] = None
        self.company_locations: Optional[List[str]] = None
        self.company_web_site: str = ''
        self.company_description: str = ''
        self.position: str = ''
        self.new_message_notified_at: Optional[datetime] = None
        self.photo_url: str = ''
        self.slack_profile = SlackProfile()
        self.leads_limit: Optional[int] = None
        self.leads_proceeded: Optional[int] = None
        self.leads_filtered: Optional[int] = None
        self.leads_limit_updated_at: Optional[int] = None
        self.keywords: Optional[List[str]] = None
        self.block_words: Optional[List[str]] = None
        self.paid_lead_price: int = 1
        self.state: int = 0
        self.credits_exceeded_at: Optional[datetime] = None
        self.unanswered_leads_period = None
        self.inactive = None
        self.slack_users: List[SlackUser] = []
        self.discord_users: List[DiscordUser] = []
        self.verified: bool = False
        self.subscription_id: ObjectId | None = None
        self.subscription_expired_at: datetime | None = None
        self.balance: str | None = None
        self.subscription_name: str | None = None

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model: UserModel = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        if '_id' in dic:
            setattr(model, 'id', dic['_id'])

        model.slack_profile = SlackProfile.from_dic(dic.get('slack_profile'))
        model.slack_users = [SlackUser.from_dic(user) for user in dic.get('slack_users', [])]
        model.discord_users = [DiscordUser.from_dic(user) for user in dic.get('discord_users', [])]
        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)

        if result.get('slack_profile', None):
            result['slack_profile'] = result.get('slack_profile').__dict__

        return result

    @property
    def is_admin(self):
        return UserRole.ADMIN in self.roles

    def get_slack_user(self, slack_email: str):
        return next(filter(lambda x: slack_email == x.email, self.slack_users), None)

    def get_discord_user(self, login: str):
        return next(filter(lambda x: login == x.login, self.discord_users), None)


class DiscordUser(BaseModel):
    pass

    def __init__(self):
        super().__init__()
        self.created_at = datetime.now(UTC)
        self.login = ''
        self.captcha_key = ''
        self.status = None
        self.workspaces: List[UserWorkspace] = []

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)

        if result.get('workspaces', None):
            result['workspaces'] = [ws.__dict__ for ws in result.get('workspaces')]

        return result

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        model.workspaces = [UserWorkspace.from_dic(ws) for ws in dic.get('workspaces', [])]
        return model


class SlackUser:
    pass

    def __init__(self):
        self.created_at = datetime.now(UTC)
        self.cookies = {}
        self.email = ''
        self.status = None
        self.workspaces: List[UserWorkspace] = []

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)

        if result.get('workspaces', None):
            result['workspaces'] = [ws.__dict__ for ws in result.get('workspaces')]

        return result

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        model.workspaces = [UserWorkspace.from_dic(ws) for ws in dic.get('workspaces', [])]
        return model


class UserWorkspace:
    pass

    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.url = ''
        self.domain = ''
        self.active_users = ''
        self.profile_photos = []
        self.associated_user = ''
        self.magic_login_url = ''
        self.magic_login_code = ''
        self.user_email = ''
        self.user_type = ''
        self.variant = ''
        self.token = ''
        self.icon = ''
        self.two_factor_required = False

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model: UserWorkspace = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        model.icon = dic.get('icon_88', "")
        return model


class UserResetPasswordModel(BaseModel):
    pass

    def __init__(self):
        super().__init__()
        self.email = None


class LeadModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.status = ''
        self.notes = ''
        self.archived = False
        self.message: Optional[MessageModel] = None
        self.hidden = False
        self.followup_date = None
        self.score = 0
        self.board_id = None
        self.linkedin_urls = []
        self.likes = 0
        self.reactions = 0
        self.replies = []
        self.last_action_at: Optional[datetime] = None
        self.slack_channel = None

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model: LeadModel = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        model.message = MessageModel.from_dic(dic['message'])
        if not model.last_action_at:
            model.last_action_at = model.created_at

        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        result["message"] = self.message.to_dic()
        result['archived'] = self.archived
        return result


class ExtendedLeadModel(LeadModel):
    def __init__(self):
        super().__init__()
        self.previous_publications = []
        self.last_conversation: List[ChatMessage] = []
        self.contact: SlackMemberInformation | None = None
        self.deleted = False
        self.user_lead: UserLeadModel | None = None
        self.dedicated: bool = False
        self.bots: List[BotInfo] = []
        self.user_contact: UserContact | None = None
        self.paid: bool = False

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        result: ExtendedLeadModel | None = LeadModel.from_dic(dic)
        if not result:
            return None

        result.contact = SlackMemberInformation.from_dic(dic.get('contact'))
        result.user_contact = UserContact.from_dic(dic.get('user_contact'))
        result.previous_publications = [LeadModel.from_dic(lead) for lead in dic.get('previous_publications', [])]
        result.user_lead = UserLeadModel.from_dic(dic.get('user_lead'))
        result.last_conversation = [ChatMessage.from_dic(message) for message in dic.get('last_conversation', [])]
        result.bots = [BotInfo.from_dic(bot) for bot in dic.get('bots', [])]
        return result

    def to_csv(self, board_name: str) -> List[str]:
        return [self.message.source, self.contact.real_name, self.contact.title, self.contact.email,
                self.notes, board_name, self.status,
                self.followup_date.strftime("%d.%m.%Y %H:%M") if self.followup_date else "",
                self.message.message.replace('\n', ' ').strip()]


class BotInfo:
    def __init__(self):
        self.id = None
        self.invalid_creds: bool | None = False
        self.source = None
        self.banned: bool | None = False
        self.user_name: str = ''
        self.associated_user: str | None = ''
        self.deleted: bool = False
        self.two_factor_required = False

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = BotInfo()
        for k, v in dic.items():
            if hasattr(model, k):
                setattr(model, k, v)

        if '_id' in dic:
            setattr(model, 'id', dic['_id'])

        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        return result


class SlackReplyModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.type = None
        self.user = None
        self.username = None
        self.text = None
        self.thread_ts = None
        self.parent_user_id = None
        self.ts = None
        self.files = []
        self.attachments = []

    @classmethod
    def from_slack_response(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)

        js_ticks = int(model.ts.split('.')[0] + model.ts.split('.')[1][3:])
        model.created_at = datetime.fromtimestamp(js_ticks / 1000.0)

        if model.files:
            model.files = [{"url_private_download": file.get("url_private_download")} for file in model.files]

        return model


class ChatMessage:
    bot_id: ObjectId
    user_id: ObjectId
    sender_id: str
    text: str
    user: str
    id: str
    viewed: bool
    files: list
    attachments: list[dict] | None
    created_at: datetime | None

    class SlackFileModel:
        def __init__(self):
            self.id = None
            self.name = None
            self.title = None
            self.filetype = None
            self.size = 0
            self.mimetype = None
            self.download_url = None

        def to_dic(self):
            result = copy.deepcopy(self.__dict__)
            return result

    def __init__(self):
        self.viewed = False
        self.text: str = ''
        self.created_at: datetime
        self.user = ''
        self.id = ''
        self.files = []
        self.attachments = []

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        if self.files and 'files' in result:
            result['files'] = [x.to_dic() if isinstance(x, ChatMessage.SlackFileModel) else x for x in self.files]

        return result

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None
        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)
        return model


class ScheduledChatMessage(ChatMessage):
    post_at: Optional[datetime]
    jib: Optional[str]

    def __init__(self):
        super(ScheduledChatMessage, self).__init__()

        self.post_at = None
        self.jib = None


class UserLeadModel(LeadModel):
    pass

    def __init__(self):
        super().__init__()
        self.order: int = 0
        self.followup_date = None
        self.user_id = None
        self.chat_viewed_at = None
        self.board_id = None

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        result: UserLeadModel | None = super().from_dic(dic)
        if not result:
            return None

        result.chat_viewed_at = dic.get('chat_viewed_at')
        return result

    @staticmethod
    def from_route(lead: LeadModel):
        model_dict = lead.to_dic()
        result = UserLeadModel.from_dic(model_dict)
        result.order = 0

        result.message = MessageModel.from_dic(model_dict['message'])
        result.chat_viewed_at = None
        return result


class ExtendedUserLeadModel(UserLeadModel):
    pass

    def __init__(self):
        super().__init__()
        self.contact: SlackMemberInformation | None = None
        self.previous_publications = []
        self.bots: List[BotInfo] = []

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        result: ExtendedUserLeadModel | None = super().from_dic(dic)
        if not result:
            return None

        result.contact = SlackMemberInformation.from_dic(dic.get('contact'))
        result.previous_publications = [LeadModel.from_dic(lead) for lead in dic.get('previous_publications', [])]
        return result

    def to_dic(self):
        result = super().to_dic()
        result["contact"] = self.contact.to_dic()
        return result

    def to_csv(self, board_name: str) -> List[str]:
        return [self.message.source, self.contact.real_name, self.contact.title, self.contact.email,
                self.notes, board_name, self.status,
                self.followup_date.strftime("%d.%m.%Y %H:%M") if self.followup_date else "",
                self.message.message.replace('\n', ' ').strip()]


class BoardModel(BaseModel):
    pass

    def __init__(self):
        super().__init__()
        self.name = None
        self.user_id = None
        self.statuses: List[BoardedStatus] = []
        self.is_primary = None
        self.default = False

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = BoardModel()
        for k, v in dic.items():
            setattr(model, k, v)

        model.id = dic.get('_id')
        model.statuses = [BoardedStatus.from_dic(status) for status in dic.get('statuses', [])]
        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        result["statuses"] = [BoardedStatus.to_dic(status) for status in self.statuses]

        for status in result['statuses']:
            status['board_id'] = result['id']

        return result


class BoardedStatus:
    pass

    def __init__(self):
        self.id = None
        self.name = None
        self.order = 0
        self.is_primary = False
        self.default = False
        self.user_leads = 0
        self.collapsed = False

    def to_dic(self):
        self.id = self.name
        return copy.deepcopy(self.__dict__)

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None
        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)
        return model


class SlackProfile:
    pass

    def __init__(self):
        self.title = ''
        self.phone = ''
        self.skype = ''
        self.display_name = ''
        self.real_name = ''
        self.email = ''

    def to_dic(self):
        return copy.deepcopy(self.__dict__)

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None
        model = cls()
        for k, v in dic.items():
            setattr(model, k, v)
        return model


class SlackMemberInformation(BaseModel, SlackProfile):
    workspace: str
    sender_id: str
    images: dict
    full_text: str
    deleted: bool = False
    is_bot: bool = False
    is_app_user: bool = False
    is_admin: bool = False
    is_owner: bool = False
    is_email_confirmed: bool = False
    online: Optional[str] = None
    online_updated_at: datetime = None
    timezone: SlackTimeZone = None
    source: Source = None

    @classmethod
    def from_dic(cls, dic: dict):
        model: SlackMemberInformation = cls()
        if not dic:
            return None

        for k, v in dic.items():
            setattr(model, k, v)

        model.online = dic.get('online', '') == "active"
        model: SlackMemberInformation | None = super().from_dic(dic)
        model.source = Source.from_dic(dic.get('source'))
        return model

    def to_dic(self):
        result = copy.deepcopy(self.__dict__)
        if result.get('source'):
            result['source'] = Source.to_dic(result.get('source'))
        return result

    @staticmethod
    def from_slack_response(slack_profile: dict, source: Source = None):
        member_info: SlackMemberInformation = SlackMemberInformation()
        member_info.source = source
        member_info.sender_id = slack_profile.get("id")
        member_info.display_name = slack_profile["profile"].get("display_name")
        member_info.real_name = slack_profile["profile"].get("real_name")
        member_info.title = slack_profile["profile"].get("title")
        member_info.phone = slack_profile["profile"].get("phone")
        member_info.skype = slack_profile["profile"].get("skype")
        member_info.email = slack_profile["profile"].get("email")
        member_info.images = {
            'image_24': slack_profile.get("profile", {}).get("image_24",
                                                             'https://a.slack-edge.com/80588/img/slackbot_24.png'),
            'image_32': slack_profile.get("profile", {}).get("image_32",
                                                             'https://a.slack-edge.com/80588/img/slackbot_32.png'),
            'image_48': slack_profile.get("profile", {}).get("image_48",
                                                             'https://a.slack-edge.com/80588/img/slackbot_48.png'),
            'image_72': slack_profile.get("profile", {}).get("image_72",
                                                             'https://a.slack-edge.com/80588/img/slackbot_72.png'),
            'image_192': slack_profile.get("profile", {}).get("image_192",
                                                              'https://a.slack-edge.com/80588/img/slackbot_192.png'),
            'image_512': slack_profile.get("profile", {}).get("image_512",
                                                              'https://a.slack-edge.com/80588/img/slackbot_512.png'),

        }
        member_info.timezone = {"tz": slack_profile.get("tz"), "tz_label": slack_profile.get("tz_label"),
                                "tz_offset": slack_profile.get("tz_offset")}
        return member_info


class UserContact(SlackMemberInformation):
    chat_id: str
    user_id: ObjectId
    source_id: str
    scheduled_messages: List[ScheduledChatMessage] = []
    last_message_at: Optional[datetime]

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None
        model: UserContact | None = super().from_dic(dic)
        model.chat_history = [ChatMessage.from_dic(message) for message in dic.get('chat_history', [])]
        model.scheduled_messages = [ScheduledChatMessage.from_dic(item) for item in dic.get("scheduled_messages", [])]
        return model


class SlackTimeZone:
    tz: Optional[str]
    tz_label: Optional[str]
    tz_offset: Optional[int]


class ExtendedSlackMemberInformation(SlackMemberInformation):
    previous_publications = []
    name: str = None
    bots: List[BotInfo] = []

    @classmethod
    def from_dic(cls, dic: dict):
        model: ExtendedSlackMemberInformation | None = super().from_dic(dic)
        if not model:
            return None

        model.previous_publications = [LeadModel.from_dic(lead) for lead in dic.get('previous_publications', [])]
        model.bots = [BotInfo.from_dic(bot) for bot in dic.get('bots', [])]
        return model

    @staticmethod
    def to_lead(contact: ExtendedSlackMemberInformation, linkedin_contacts: Dict[str, LinkedinContact] = None) \
            -> ExtendedUserLeadModel:
        lead = ExtendedUserLeadModel()
        lead.id = str(contact.id)
        lead.created_at = contact.created_at
        lead.notes = ""
        lead.slack_channel = None
        lead.hidden = True
        lead.replies = []
        lead.reactions = 0
        lead.last_action_at = datetime.now(UTC)
        lead.created_at = datetime.now(UTC)
        if not hasattr(contact, "real_name"):
            contact.real_name = contact.name
        if not hasattr(contact, "display_name"):
            contact.display_name = contact.name

        lead.linkedin_urls = [linkedin_contacts[contact.sender_id].urls[0].get("url")] \
            if linkedin_contacts and contact.sender_id in linkedin_contacts \
            else [get_linkedin_search_contact(contact.real_name)]
        lead.message = MessageModel()
        lead.message.message = contact.real_name
        if contact.title:
            lead.message.message += contact.title
        lead.message.message_id = str(contact.id)
        lead.message.name = contact.source.source_name
        lead.message.source = contact.source
        lead.message.sender_id = contact.sender_id
        lead.message.companies = []
        lead.message.technologies = []
        lead.message.locations = []
        lead.message.chat_history = []
        lead.chat_viewed_at = datetime.now(UTC)
        lead.chat_history = []
        lead.previous_publications = contact.previous_publications if hasattr(contact, "previous_publications") else []
        lead.bots = contact.bots if hasattr(contact, "bots") else []
        lead.contact = contact
        return lead


class UserTemplateModel(BaseModel):
    text: str
    subject: Optional[str]
    user_id: Optional[ObjectId]


class LinkedinContact(BaseModel):
    full_name: str
    slack_user: str
    title: str
    urls: List[dict]


class CloudFileModel(BaseModel):
    blob_path: str
    public_url: str
    file_name: str

    def __init__(self, blob_path: str, public_url: str, file_name: str):
        super().__init__()
        if not self.id:
            self.id = str(ObjectId())
        self.blob_path = blob_path
        self.public_url = public_url
        self.file_name = file_name


class GroupedMessagesModel:
    messages: List[ChatMessage] = []

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None

        model = cls()
        model.messages = [ChatMessage.from_dic(message) for message in dic.get('messages', [])]
        return model


class UserVerificationModel(DictionaryModel):
    pass

    def __init__(self):
        super().__init__()
        self.email = None
        self.created_at = datetime.now(UTC)


class UsersPage:
    users: List[UserModel]
    count: int = 0

    def __init__(self, users: List[UserModel], count: int):
        self.users = users
        self.count = count

    @staticmethod
    def from_dic(dic: dict):
        users = [UserModel.from_dic(doc) for doc in dic.get('page', [])]
        count = dic.get('count', 0)
        return UsersPage(users=users, count=count)


class Feature(DictionaryModel):
    display_name: str
    name: FeaturesEnum
    description: str | None = None
    limit: int | None = None
    options: FeatureOptions | None = None


class Subscription(BaseModel):
    features: list[Feature]
    duration_days: int
    name: str
    price: int
    limits: int
    trial: bool
    updated_at: datetime = None

    @classmethod
    def from_dic(cls, dic: dict):
        if not dic:
            return None
        model: Subscription | None = super().from_dic(dic)
        model.features = [Feature.from_dic(feature) for feature in dic.get('features', [])]
        return model
