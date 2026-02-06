from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/', blog, name='blog'),
    path('faq/', faq, name='faq'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('team/', team, name='team'),
    path('values/', values, name='values'),
    # project
    path('project/<int:project_id>/', project_detail, name='project_detail'),
    path('projects/', projects, name='projects'),
    # pack
    path('business-pack/', business_pack, name='business_pack'),
    path('assistance-pack/', assistance_pack, name='assistance_pack'),
    path('internship-pack/', internship_pack, name='internship_pack'),
    path('personal-pack/', personal_pack, name='personal_pack'),
    path('professional-pack/', professional_pack, name='professional_pack'),
    path('scholarship-pack/', scholarship_pack, name='scholarship_pack'),
    path('sharing-pack/', sharing_pack, name='sharing_pack'),
    path('learning-with-us/', learning_with_us, name='learning_with_us'),
    path('become-member/', become_member, name='become_member'),
    path('ressources-pack/', ressources_pack, name='ressources_pack'),
    path('mentor-pack/', mentor_pack, name='mentor_pack'),

#     message
    path('messages/', messages, name='messages'),
    path('envoyer_message', envois_message, name='envois')

    
    
]