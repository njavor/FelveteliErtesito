from django.shortcuts import render
from django.contrib.auth import authenticate
from felvetel.models import Jelentkezo, Tagozat

def index(request):
    template = 'index.html'
    van = 'dontes.html'
    nincs = 'nincs.html'

    postE = request.method == "POST"
    if postE:
        azon = request.POST['oAzonosito']
        jelentkezo = Jelentkezo.objects.filter(azonosito = azon).first()
        

        if jelentkezo != None:
            felveteliSiker = {}
            for jelolttagozat in jelentkezo.tagozatok.all():
                match jelolttagozat.rov:
                    case "A":
                        adottPont = jelentkezo.A
                    case "B":
                        adottPont = jelentkezo.B
                    case "C1":
                        adottPont = jelentkezo.C1
                    case "C2":
                        adottPont = jelentkezo.C2
                    case "D1":
                        adottPont = jelentkezo.D1
                    case "D2":
                        adottPont = jelentkezo.D2
                    case "E":
                        adottPont = jelentkezo.E
                    case "F1":
                        adottPont = jelentkezo.F1
                    case "F2":
                        adottPont = jelentkezo.F2
                felveteliSiker[jelolttagozat.nev] = [adottPont, "nem nyert felvételt"]
                for felvetttagozat in jelentkezo.felveve.all():
                    if jelolttagozat.nev == felvetttagozat.nev:
                        felveteliSiker[jelolttagozat.nev] = [adottPont, "felvételt nyert"]


            context = {'Viki': jelentkezo, 'tagozats': felveteliSiker }
            return render(request, van, context)    
        else :
            return render(request, nincs)
    else:
        return render(request, template)


def uploadcsvview(request):
    template = 'admin/upload_csv.html'

    if request.method == "POST":
        user = authenticate(username='admin', password=request.POST['jelszo'])
        if user is not None:
            csvDok = request.POST['csvSz']
            csv_data = csvDok.split("\n")

            for x in csv_data:
                fields = x.split(",")
                if len(fields) < 18:
                    return render(request, template, {'rovid': True})
                else:
                    krealt = Jelentkezo.objects.create(
                        azonosito = fields[0],
                        nev = fields[1],
                        A = float(fields[2]),
                        B = float(fields[4]),
                        C1 = float(fields[6]),
                        C2 = float(fields[8]),
                        D1 = float(fields[10]),
                        D2 = float(fields[12]),
                        E = float(fields[14]),
                        F1 = float(fields[16]),
                        F2 = float(fields[18]),
                    )

                betulista = ['A', 'B', 'C1', 'C2', 'D1', 'D2', 'E', 'F1', 'F2']
                i = 0
                for j in range(9):
                    adott = (i+1)*2
                    if float(fields[adott]) > 0:
                        krealt.tagozatok.add(Tagozat.objects.get(rov=betulista[i]))
                        if fields[adott+1] == 'True':
                            krealt.felveve.add(Tagozat.objects.get(rov=betulista[i]))
                    i += 1
            return render(request, template, {'igen': True})
        else:
            return render(request, template, {'nope': True})
    else:
        return render(request, template, {})
