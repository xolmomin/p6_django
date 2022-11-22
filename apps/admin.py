# from django.contrib import admin
# from django.contrib.admin import ModelAdmin, TabularInline
# from import_export.admin import ImportExportModelAdmin
# from import_export.resources import ModelResource
#
# from apps.models import Blog, Region
#
# # admin.site.register(Region)
# # admin.site.register(Blog)
#
#
# class RegionResource(ModelResource):
#     class Meta:
#         model = Region
#
#
# class RegionAdminImportExportModelAdmin(ImportExportModelAdmin):
#     resource_classes = [RegionResource]
#
#
# admin.site.register(Region, RegionAdminImportExportModelAdmin)
#
# #
# #
# # @admin.register(Region)
# # class RegionAdmin(ModelAdmin):
# #     list_display = ('id', 'name')
# #
# #     def has_add_permission(self, request):
# #         return False
# #
# #     # def has_delete_permission(self, request, obj=None):
# #     #     return False
# #
# #
# # # class CategoryTabularInline(TabularInline):
# # #     model = Category
# # #     extra = 2
# # #     min_num = 1
# # #
# #
# # @admin.register(Hero)
# # class HeroAdmin(ModelAdmin):
# #     list_display = ('name', 'id')
# #     # inlines = (CategoryTabularInline, )
#
#
# from django.contrib.admin import AdminSite
#
#
# class ModeratorAdminSite(AdminSite):
#     site_header = "Moderatorlar uchun bo`lim"
#     site_title = "Moderatorlar"
#     index_title = "Moderator bo`limiga xush kelibsiz!"
#
#
# moderator_admin_site = ModeratorAdminSite(name='moderator_admin')
#
#
# # moderator_admin_site.register(Blog)
#
#
#
# @admin.register(Blog, site=moderator_admin_site)
# class RegionAdmin(ModelAdmin):
#     list_display = ('id', 'name')
#
# # event_admin_site.register(Event)
# # event_admin_site.register(EventHero)
# # event_admin_site.register(EventVillain)
