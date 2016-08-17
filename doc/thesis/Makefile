# Makefile - Documento de Tesis
#
# autor: Carlos Alberto Llano R.
# fecha: Jun. 22/2013
# ultima modificacion: Jun. 22/2013
#

SRC = tesis.tex

article:
	pdflatex articulo.tex
	pdflatex articulo.tex
	mv articulo.pdf Shortpaper#80.pdf
	evince Shortpaper#80.pdf

pdf: clean
	pdflatex tesis.tex
	pdflatex tesis.tex
	evince tesis.pdf

slides:
	make -C presentation/

clean:
	rm -f *.log
	rm -f *.out
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
	cd presentation; make clean; cd ..

clean2:
	rm -f *.log
	rm -f *.out
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

