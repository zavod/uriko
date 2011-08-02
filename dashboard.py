from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name

from cms.dashboard import CmsIndexDashboard


class CustomIndexDashboard(CmsIndexDashboard):
    """
    Custom index dashboard for zavod.
    """
    pass
