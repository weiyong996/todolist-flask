from flask import flash, redirect, url_for, render_template, abort, request

from todolist import app, db
from todolist.models import Item, CompletedItem
from todolist.forms import ItemForm, CompleteAndDeleteForm, EditItemForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ItemForm()
    complete_delete_form = CompleteAndDeleteForm()
    items = Item.query.order_by(Item.timestamp.desc()).all()
    completed_items = CompletedItem.query.order_by(CompletedItem.timestamp.desc()).all()
    return render_template('index.html', form=form,complete_delete_form=complete_delete_form,items=items, completed_items=completed_items)


@app.route('/add', methods=['POST'])
def add():
    form = ItemForm()
    if form.validate_on_submit():
        content = form.content.data
        item = Item(content=content)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/completed/<int:item_id>')
def completed(item_id):
    item = Item.query.get(item_id)
    completed_item = CompletedItem(content=item.content)
    db.session.delete(item)
    db.session.add(completed_item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/back_todo/<int:completed_item_id>')
def back_todo(completed_item_id):
    completed_item = CompletedItem.query.get(completed_item_id)
    item = Item(content=completed_item.content)
    db.session.add(item)
    db.session.delete(completed_item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_completed_item/<int:completed_id>')
def delete_completed_item(completed_id):
    completed_item = CompletedItem.query.get(completed_id)
    db.session.delete(completed_item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    edit_form = EditItemForm(request.form)
    edit_item = Item.query.get(item_id)
    print(11111, request.method, edit_form.validate(), edit_form.content.data)
    if edit_form.validate_on_submit():
        print(22222)
        edit_item.content = edit_form.content.data
        db.session.commit()
        return redirect(url_for('index'))
    edit_form.content.data = edit_item.content
    return render_template('edit.html', edit_form=edit_form)
