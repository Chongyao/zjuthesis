sed -i 's/ \[1\]/~\\cite{hughes2012finite}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[2\]/~\\cite{bathe2006finite}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[3\]/~\\cite{nealen2006physically}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[4\]/~\\cite{todorov2012mujoco}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[5\]/~\\cite{huang2025stiffgipc}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[6\]/~\\cite{saad2003iterative}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[7\]/~\\cite{bridson2002robust}/g' body/graduate/intro/1_background.tex
sed -i 's/ \[8\]/~\\cite{Shewchuk2002whatIsAGoodLinearFiniteElement}/g' body/graduate/intro/1_background.tex

# add citations to bib
cat << 'BIB' >> body/ref.bib

@book{hughes2012finite,
  title={The finite element method: linear static and dynamic finite element analysis},
  author={Hughes, Thomas JR},
  year={2012},
  publisher={Courier Corporation}
}

@book{bathe2006finite,
  title={Finite element procedures},
  author={Bathe, Klaus-J{\"u}rgen},
  year={2006},
  publisher={Klaus-Jurgen Bathe}
}

@article{nealen2006physically,
  title={Physically based deformable models in computer graphics},
  author={Nealen, Andrew and M{\"u}ller, Matthias and Keiser, Richard and Boxerman, Eddy and Carlson, Mark},
  journal={Computer graphics forum},
  volume={25},
  number={4},
  pages={809--836},
  year={2006},
  organization={Wiley Online Library}
}

@inproceedings{todorov2012mujoco,
  title={Mujoco: A physics engine for model-based control},
  author={Todorov, Emanuel and Erez, Tom and Tassa, Yuval},
  booktitle={2012 IEEE/RSJ international conference on intelligent robots and systems},
  pages={5026--5033},
  year={2012},
  organization={IEEE}
}

@book{saad2003iterative,
  title={Iterative methods for sparse linear systems},
  author={Saad, Yousef},
  year={2003},
  publisher={SIAM}
}
BIB
