# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('todo_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('todo', ['Tag'])

        # Adding model 'ToDoItem'
        db.create_table('todo_todoitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('details', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('excellence', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('importance', self.gf('django.db.models.fields.IntegerField')(default='0', max_length=1)),
            ('due', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='todos_created', to=orm['auth.User'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('todo', ['ToDoItem'])

        # Adding M2M table for field interests on 'ToDoItem'
        db.create_table('todo_todoitem_interests', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('todoitem', models.ForeignKey(orm['todo.todoitem'], null=False)),
            ('interest', models.ForeignKey(orm['profiles.interest'], null=False))
        ))
        db.create_unique('todo_todoitem_interests', ['todoitem_id', 'interest_id'])

        # Adding M2M table for field tags on 'ToDoItem'
        db.create_table('todo_todoitem_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('todoitem', models.ForeignKey(orm['todo.todoitem'], null=False)),
            ('tag', models.ForeignKey(orm['todo.tag'], null=False))
        ))
        db.create_unique('todo_todoitem_tags', ['todoitem_id', 'tag_id'])

        # Adding M2M table for field users_claimed on 'ToDoItem'
        db.create_table('todo_todoitem_users_claimed', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('todoitem', models.ForeignKey(orm['todo.todoitem'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('todo_todoitem_users_claimed', ['todoitem_id', 'user_id'])

        # Adding M2M table for field sub_tasks on 'ToDoItem'
        db.create_table('todo_todoitem_sub_tasks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_todoitem', models.ForeignKey(orm['todo.todoitem'], null=False)),
            ('to_todoitem', models.ForeignKey(orm['todo.todoitem'], null=False))
        ))
        db.create_unique('todo_todoitem_sub_tasks', ['from_todoitem_id', 'to_todoitem_id'])

        # Adding model 'Update'
        db.create_table('todo_update', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('todoitem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.ToDoItem'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('todo', ['Update'])

        # Adding model 'Comment'
        db.create_table('todo_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('todoitem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['todo.ToDoItem'])),
            ('_order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('todo', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('todo_tag')

        # Deleting model 'ToDoItem'
        db.delete_table('todo_todoitem')

        # Removing M2M table for field interests on 'ToDoItem'
        db.delete_table('todo_todoitem_interests')

        # Removing M2M table for field tags on 'ToDoItem'
        db.delete_table('todo_todoitem_tags')

        # Removing M2M table for field users_claimed on 'ToDoItem'
        db.delete_table('todo_todoitem_users_claimed')

        # Removing M2M table for field sub_tasks on 'ToDoItem'
        db.delete_table('todo_todoitem_sub_tasks')

        # Deleting model 'Update'
        db.delete_table('todo_update')

        # Deleting model 'Comment'
        db.delete_table('todo_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.interest': {
            'Meta': {'ordering': "['name']", 'object_name': 'Interest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'todo.comment': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Comment'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'todoitem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.ToDoItem']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'todo.tag': {
            'Meta': {'ordering': "['name']", 'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'todo.todoitem': {
            'Meta': {'ordering': "['-creation_date']", 'object_name': 'ToDoItem'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todos_created'", 'to': "orm['auth.User']"}),
            'details': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'due': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'excellence': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': "'0'", 'max_length': '1'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['profiles.Interest']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sub_tasks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sub_tasks_rel_+'", 'blank': 'True', 'to': "orm['todo.ToDoItem']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['todo.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'users_claimed': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'todos_claimed'", 'blank': 'True', 'to': "orm['auth.User']"})
        },
        'todo.update': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Update'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'todoitem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['todo.ToDoItem']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['todo']