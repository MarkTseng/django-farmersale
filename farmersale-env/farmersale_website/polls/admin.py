from django.contrib import admin
from polls.models import Question, Choice

admin.site.register(Choice)

# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date','question_text']
	fieldsets = [
			(None,{'fields':['question_text']}),
			('Date info', {'fields':['pub_date']}),
			]
	inlines = [ChoiceInline]
	
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	#template = 'admin/base_site.html'


admin.site.register(Question,QuestionAdmin)
#admin.site.register(Question)
