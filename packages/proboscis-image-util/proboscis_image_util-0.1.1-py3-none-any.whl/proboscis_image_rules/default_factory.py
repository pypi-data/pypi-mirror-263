from omni_converter import AutoDataFactory
from omni_cv_rules.rulebook import CV_RULEBOOK
from proboscis_image_rules.default_rule import ARCHPAINTER_RULES

_factory = AutoDataFactory(CV_RULEBOOK + ARCHPAINTER_RULES)
