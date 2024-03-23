from praetorian_cli.sdk.test import BaseTest
from praetorian_cli.sdk.test.resources.utils import Utils


class TestRisk(BaseTest):

    def setup_class(self):
        self.chaos, self.username = BaseTest.setup_chaos(self)
        self.seed = "contoso.com"
        self.finding = "Foobar Finding"
        self.utils = Utils(self.chaos)

    def test_risk(self):
        self.utils.add_seed(self.seed)
        response = self.utils.wait_for_composite(dict(composite=f'#asset#{self.seed}'))
        assert response, "Received empty response for my Assets"

        self.chaos.add_risk(dict(composite=f'#asset#{self.seed}'), self.finding)
        my_risk = self.chaos.my(dict(composite=f'#risk#{self.seed}'))
        assert my_risk is not None
        self.utils.freeze_seed(self.seed)


