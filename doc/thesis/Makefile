# Makefile - Documento de Tesis
#
# autor: Carlos Alberto Llano R.
# fecha: Jun. 22/2013
# ultima modificacion: Jun. 22/2013
#

SRC = main.tex configuracion.tex titulo.tex abstract.tex agradecimientos.tex introduccion.tex enfoquesaprov.tex apirest.tex diseno.tex implementacion.tex conclusiones.tex anexos.tex pruebas.tex csthesis.cls

main.dvi: $(SRC) main.bbl
	rm -f *.ind
	rm -f *.idx
	latex main
	latex main
	makeindex main
	latex main

pdf: main.dvi
	dvips -o Tesis.ps main.dvi -t letter
	ps2pdf Tesis.ps
	evince Tesis.pdf

force:
	latex main

run: main.dvi
	xdvi main.dvi

main.bbl: bibliografia.bib
	latex main
	bibtex main

clean:
	rm -f *.log
	rm -f *.aux
	rm -f *.toc
	rm -f *.dvi
	rm -f *.blg
	rm -f *~
	rm -f *.lot
	rm -f *.lof
	rm -f *.loa
	rm -f *.ps
	rm -f *.pdf
	rm -f *.idx
	rm -f *.ind
	rm -f *.ilg

clean2:
	rm -f *.log
	rm -f *.aux
	rm -f *.toc
	rm -f *.dvi
	rm -f *.blg
	rm -f *~
	rm -f *.lot
	rm -f *.lof
	rm -f *.loa
	rm -f *.ps
	rm -f *.idx
	rm -f *.ind
	rm -f *.ilg

