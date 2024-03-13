from .models import Color
from .models import ProductHaveImages
from .serializers import ProductHaveImagesSerializer

#Function to get or create color
def get_or_create_color(color_names):
    color_ids = []
    for color_name in color_names:
        color_instance, created = Color.objects.get_or_create(name=color_name)
        color_ids.append(color_instance.id)
    return color_ids


#Helper function to create and link image with product
def create_image(images,product_id):
    image_data=[]
    dict_data = {
           'user':product_id,
           'image':images,
       }
    image_data.append(dict_data)
    if len(image_data)>0:        
        image_serializer = ProductHaveImagesSerializer(many=True,data=image_data)
        image_serializer.is_valid(raise_exception=True)
        image_serializer.save() 
    return True