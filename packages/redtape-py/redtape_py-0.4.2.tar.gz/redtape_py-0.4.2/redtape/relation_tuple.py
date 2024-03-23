from itertools import groupby
from operator import attrgetter
from typing import NamedTuple


class RelationTuple(NamedTuple):
    subject: str
    relation: str
    resource: str


SUBJECT_KEY = attrgetter("subject")


class RelationGraph:
    def __init__(self, relation_tuples: list[RelationTuple]):
        self._relation_tuples = relation_tuples
        self._subject_relation_tuples = {}

        for k, g in groupby(relation_tuples, key=SUBJECT_KEY):
            group_members = list(g)
            self._subject_relation_tuples[k] = (
                {(rt.relation, rt.resource) for rt in group_members},
                {rt.resource for rt in group_members if rt.relation == "member"},
            )

    def check(self, relation_tuple: RelationTuple):
        """Check if the given RelationTuple is part of this RelationGraph."""
        (subject, relation, resource) = relation_tuple

        check = (relation, resource) in self._subject_relation_tuples[subject][0]
        if check is True:
            return True

        visited = {subject}
        to_check = list(self._subject_relation_tuples[subject][1])

        while to_check:
            next = to_check.pop()

            if next not in visited:
                check = (relation, resource) in self._subject_relation_tuples[next][0]
                if check is True:
                    return True

                to_check = to_check.extend(self._subject_relation_tuples[next][1])
                visited.add(next)

        return False
