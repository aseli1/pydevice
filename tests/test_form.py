from dm_requests import DeviceMagic
from .test_object import test_object, test_form
import vcr

dm = test_object

@vcr.use_cassette('fixtures/cassettes/form/all')
def test_all():
    response = dm.form.all()
    assert isinstance(response, dict)

@vcr.use_cassette('fixtures/cassettes/form/details')
def test_details():
    response = dm.form.details(test_form['form_id'])
    assert isinstance(response, dict)

@vcr.use_cassette('fixtures/cassettes/form/create')
def test_create():
    response = dm.form.create(test_form['sample_form'])
    assert response, "Form created"

@vcr.use_cassette('fixtures/cassettes/form/update')
def test_update():
    response = dm.form.update(test_form['form_id'], test_form['sample_form'])
    assert response, "Form updated"

@vcr.use_cassette('fixtures/cassettes/form/delete')
def test_delete():
    response = dm.form.delete(test_form['delete_id'])
    assert response, "Form deleted"

@vcr.use_cassette('fixtures/cassettes/form/new_group')
def test_new_group():
    response = dm.form.new_group(test_form['form_id'], test_form['group_json'])
    assert response, "Form group updated"