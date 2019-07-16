from django.http import Http404

def get_all_objects(self):
    return self.model.objects.all()

def get_object(self, pk):
    try:
        return self.model.objects.get(pk=pk)
    except self.model.DoesNotExist:
        raise Http404