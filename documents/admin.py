from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
@admin.register(Agreements)
class AgreementsAdmin(admin.ModelAdmin):
    list_display=('id','agreements_image_booking_agreements','agreements_image_main_agreements','project_details')
    fields = ('booking_agreements','main_agreements','project_details')
    list_per_page=10
    search_fields = ('id',)

    def agreements_image_booking_agreements(self,obj):
        return format_html(f'<img src="/media/{obj.booking_agreements}" style=height:50px;width:50px>')

    def agreements_image_main_agreements(self,obj):
        return format_html(f'<img src="/media/{obj.main_agreements}" style=height:50px;width:50px>')

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display=('id','documents_image_boq','documents_image_payments','documents_image_projects_schedule','documents_image_quality_checkList','documents_image_specifications','project_details')
    list_per_page=10
    search_fields = ('id',)

    def documents_image_boq(self,obj):
        return format_html(f'<img src="/media/{obj.boq}" style=height:50px;width:50px>')

    def documents_image_payments(self,obj):
        return format_html(f'<img src="/media/{obj.payments}" style=height:50px;width:50px>')

    def documents_image_projects_schedule(self,obj):
        return format_html(f'<img src="/media/{obj.projects_schedule}" style=height:50px;width:50px>')

    def documents_image_quality_checkList(self,obj):
        return format_html(f'<img src="/media/{obj.quality_checkList}" style=height:50px;width:50px>')

    def documents_image_specifications(self,obj):
        return format_html(f'<img src="/media/{obj.specifications}" style=height:50px;width:50px>')


@admin.register(ConceptPlans)
class ConceptPlansAdmin(admin.ModelAdmin):
    list_display=('id','concept_image_concept_plans','project_details')
    fields=('concept_plans','project_details')
    list_per_page=10
    search_fields = ('id',)

    def concept_image_concept_plans(self,obj):
        return format_html(f'<img src="/media/{obj.concept_plans}" style=height:50px;width:50px>')


@admin.register(WorkingDrawings)
class WorkingDrawingsAdmin(admin.ModelAdmin):
    list_display=('id','working_image_open_schedule','working_image_joinery_details',
    'working_image_plumbing_details','working_image_electrical','working_image_section',
    'working_image_section_elevation','working_image_toilet_detailing','working_image_brick_work_layout',
    'project_details')
    list_per_page=10
    search_fields = ('id',)

    def working_image_open_schedule(self,obj):
        return format_html(f'<img src="/media/{obj.open_schedule}" style=height:50px;width:50px>')

    def working_image_joinery_details(self,obj):
        return format_html(f'<img src="/media/{obj.joinery_details}" style=height:50px;width:50px>')

    def working_image_plumbing_details(self,obj):
        return format_html(f'<img src="/media/{obj.plumbing_details}" style=height:50px;width:50px>')

    def working_image_electrical(self,obj):
        return format_html(f'<img src="/media/{obj.electrical}" style=height:50px;width:50px>')

    def working_image_section(self,obj):
        return format_html(f'<img src="/media/{obj.section}" style=height:50px;width:50px>')

    def working_image_section_elevation(self,obj):
        return format_html(f'<img src="/media/{obj.section_elevation}" style=height:50px;width:50px>')

    def working_image_toilet_detailing(self,obj):
        return format_html(f'<img src="/media/{obj.toilet_detailing}" style=height:50px;width:50px>')

    def working_image_brick_work_layout(self,obj):
        return format_html(f'<img src="/media/{obj.brick_work_layout}" style=height:50px;width:50px>')


@admin.register(StructuralDrawings)
class StructuralDrawingsAdmin(admin.ModelAdmin):
    list_display=('id','structural_image_center_line_plan','structural_image_footing_layout',
    'structural_image_column_details','structural_image_plinth_beam_details','structural_image_beam_layout',
    'structural_image_slab_details','structural_image_staircase_details','project_details')
    list_per_page=10
    search_fields = ('id',)

    def structural_image_center_line_plan(self,obj):
        return format_html(f'<img src="/media/{obj.center_line_plan}" style=height:50px;width:50px>')

    def structural_image_footing_layout(self,obj):
        return format_html(f'<img src="/media/{obj.footing_layout}" style=height:50px;width:50px>')

    def structural_image_column_details(self,obj):
        return format_html(f'<img src="/media/{obj.column_details}" style=height:50px;width:50px>')

    def structural_image_plinth_beam_details(self,obj):
        return format_html(f'<img src="/media/{obj.plinth_beam_details}" style=height:50px;width:50px>')

    def structural_image_beam_layout(self,obj):
        return format_html(f'<img src="/media/{obj.beam_layout}" style=height:50px;width:50px>')

    def structural_image_slab_details(self,obj):
        return format_html(f'<img src="/media/{obj.slab_details}" style=height:50px;width:50px>')

    def structural_image_staircase_details(self,obj):
        return format_html(f'<img src="/media/{obj.staircase_details}" style=height:50px;width:50px>')

    
@admin.register(ThreeDModel)
class ThreeDModelAdmin(admin.ModelAdmin):
    list_display=('id','three_d_image_three_d_elevation','project_details')
    fields = ('three_d_elevation','project_details')

    list_per_page=10
    search_fields = ('id',)

    def three_d_image_three_d_elevation(self,obj):
        return format_html(f'<img src="/media/{obj.three_d_elevation}" style=height:50px;width:50px>')


class InsideStackAdmin(admin.StackedInline):
    model=InsideImage
class OutsideStackAdmin(admin.StackedInline):
    model=OutsideImage
class TwoDStackAdmin(admin.StackedInline):
    model=TwoD
class ThreeDStackAdmin(admin.StackedInline):
    model=ThreeD

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    inlines = (InsideStackAdmin,OutsideStackAdmin,TwoDStackAdmin,ThreeDStackAdmin)
    list_display=('id','user_name','project_details')
    list_per_page=10
    search_fields = ('id',)

    def inside_image(self,obj):
        return format_html(f'<img src="/media/{obj.inside}" style=height:50px;width:50px>')
    def outside_image(self,obj):
        return format_html(f'<img src="/media/{obj.outside}" style=height:50px;width:50px>')
    def two_d_image_image(self,obj):
        return format_html(f'<img src="/media/{obj.two_d_image}" style=height:50px;width:50px>')
    def three_d_image_image(self,obj):
        return format_html(f'<img src="/media/{obj.three_d_image}" style=height:50px;width:50px>')
