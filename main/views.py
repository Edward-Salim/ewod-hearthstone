from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi': 'Ewod Hearthstone TCG',
        'nama': 'Edward Salim',
        'kelas': 'PBP F'
    }

    return render(request, "main.html", context)