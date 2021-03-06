"""Mongodb implementations of assessment rules."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package mongo package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from .. import utilities
from ...abstract_osid.assessment import rules as abc_assessment_rules
from ..primitives import Id
from dlkit.abstract_osid.osid import errors
from dlkit.mongo.osid import rules as osid_rules




class Response(abc_assessment_rules.Response, osid_rules.OsidCondition):
    """A response to an assessment item.


    This interface contains methods to set values in response to an
    assessmet item and mirrors the item record structure with the
    corresponding setters.


    """


    _record_type_data_sets = {}
    _namespace = 'assessment.Response'


    def __init__(self, answer, **kwargs):
        self._my_answer = answer
        self._records = dict()
        # Consider that responses may want to have their own records separate
        # from the enclosed Answer records:
        self._record_type_data_sets = self._get_registry('RESPONSE_RECORD_TYPES')
        response_map = answer.object_map
        self._load_records(response_map['recordTypeIds'])


    def _load_records(self, record_type_idstrs):
        for record_type_idstr in record_type_idstrs:
            self._init_record(record_type_idstr)


    def __iter__(self):
        for attr in dir(self):
            if not attr.startswith('__'):
                yield attr


    def __getitem__(self, item):
        return getattr(self, item)


    def __getattr__(self, name):
        if not name.startswith('__'):
            try:
                return getattr(self._my_answer, name)
            except:
                raise
    def get_item_id(self):
        """Gets the ``Id`` of the ``Item``.


        return: (osid.id.Id) - the assessment item ``Id``
        *compliance: mandatory -- This method must be implemented.*


        """
        return Id(self._my_answer._my_map['itemId'])

    item_id = property(fget=get_item_id)

    def get_item(self):
        """Gets the ``Item``.


        return: (osid.assessment.Item) - the assessment item
        *compliance: mandatory -- This method must be implemented.*


        """
        # So, why would we ever let an AssessmentSession user get the Item???
        raise errors.PermissionDenied()

    item = property(fget=get_item)

    @utilities.arguments_not_none
    def get_response_record(self, item_record_type):
        """Gets the response record corresponding to the given ``Item`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``item_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(item_record_type)``
        is ``true`` .


        arg:    item_record_type (osid.type.Type): an item record type
        return: (osid.assessment.records.ResponseRecord) - the response
                record
        raise:  NullArgument - ``item_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(item_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        if not self.has_record_type(item_record_type):
            raise errors.Unsupported()
        if str(item_record_type) not in self._records:
            raise errors.Unimplemented()
        return self._records[str(item_record_type)]


