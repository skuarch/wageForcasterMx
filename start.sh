ANACONDA_HOME=~/Applications/anaconda3
source $ANACONDA_HOME/etc/profile.d/conda.sh
conda init bash
export PATH=$ANACONDA_HOME/bin:$PATH
conda activate wageForcasterMx
jupyter notebook .
