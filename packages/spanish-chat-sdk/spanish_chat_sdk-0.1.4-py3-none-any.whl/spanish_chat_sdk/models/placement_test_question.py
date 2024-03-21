from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.placement_test_follow_up_question import PlacementTestFollowUpQuestion


T = TypeVar("T", bound="PlacementTestQuestion")


@_attrs_define
class PlacementTestQuestion:
    """
    Attributes:
        cefr_level (str):
        sentence (str):
        follow_up_questions (List['PlacementTestFollowUpQuestion']):
    """

    cefr_level: str
    sentence: str
    follow_up_questions: List["PlacementTestFollowUpQuestion"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cefr_level = self.cefr_level

        sentence = self.sentence

        follow_up_questions = []
        for follow_up_questions_item_data in self.follow_up_questions:
            follow_up_questions_item = follow_up_questions_item_data.to_dict()
            follow_up_questions.append(follow_up_questions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cefr_level": cefr_level,
                "sentence": sentence,
                "follow_up_questions": follow_up_questions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.placement_test_follow_up_question import PlacementTestFollowUpQuestion

        d = src_dict.copy()
        cefr_level = d.pop("cefr_level")

        sentence = d.pop("sentence")

        follow_up_questions = []
        _follow_up_questions = d.pop("follow_up_questions")
        for follow_up_questions_item_data in _follow_up_questions:
            follow_up_questions_item = PlacementTestFollowUpQuestion.from_dict(follow_up_questions_item_data)

            follow_up_questions.append(follow_up_questions_item)

        placement_test_question = cls(
            cefr_level=cefr_level,
            sentence=sentence,
            follow_up_questions=follow_up_questions,
        )

        placement_test_question.additional_properties = d
        return placement_test_question

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
