from django.contrib import admin
from .models import MasRider, CompetitionHistory, Ability


class CompetitionInline(admin.TabularInline):
    model = CompetitionHistory
    extra = 1


class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 1


@admin.register(MasRider)
class MasRiderAdmin(admin.ModelAdmin):
    list_display = ['alias', 'name', 'age', 'series', 'organization']
    list_filter = ['series']
    search_fields = ['name', 'alias', 'organization']
    inlines = [AbilityInline, CompetitionInline]


@admin.register(CompetitionHistory)
class CompetitionHistoryAdmin(admin.ModelAdmin):
    list_display = ['rider', 'opponent', 'event_name', 'event_date', 'result']
    list_filter = ['result']


@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'rider', 'power_level']
