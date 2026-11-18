from django.core.management.base import BaseCommand

from apps.deploy.utils import ITERATION_AUTO_CLOSE_DAYS, auto_close_idle_iterations


class Command(BaseCommand):
    help = '关闭超过指定天数没有任何发布动作的迭代'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=ITERATION_AUTO_CLOSE_DAYS,
            help=f'无发布动作的天数，默认 {ITERATION_AUTO_CLOSE_DAYS}',
        )

    def handle(self, *args, **options):
        closed_ids = auto_close_idle_iterations(days=options['days'])
        self.stdout.write(f'已关闭 {len(closed_ids)} 个迭代: {closed_ids}')
