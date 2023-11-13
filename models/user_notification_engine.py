from odoo import _, api, exceptions, fields, models

from odoo.addons.bus.models.bus import channel_with_db, json_dump

DEFAULT_MESSAGE = "Default message"

SUCCESS = "success"
DANGER = "danger"
WARNING = "warning"
INFO = "info"
DEFAULT = "default"


class UserNotificationEngine(models.Model):
    _name = "user.notification.engine"

    name = fields.Char(string="Notification title")
    model_id = fields.Many2one('ir.model', string="Model")
    user_ids = fields.Many2many('res.users', string='Users')
    action = fields.Selection([
        ('create', _('Create')),
        ('update', _('Update')),
        ('delete', _('Delete')),
    ])
    update_action_fields_ids = fields.Many2many('ir.model.fields', copy=False, string="Fields",
                                                help="when one of those fields is change, notification will be display")
    notification_detail_ids = fields.Many2many('ir.model.fields', copy=False,
                                               string="value of fields will be appears in notification")
    color = fields.Char()
    limit_time = fields.Integer(string="limit time who the notification appears")
    activity = fields.Many2one("mail.activity.type", string="Type of activity",
                               help="When user isn't connected, the notification became activity")
