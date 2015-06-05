
passwd
sudo apt-get install -y git

sftp johndoe@192.168.107.42 <<EOF
get -r NS3-SOP-Simulation
get -r ns-allinone-3.21
EOF

rm ~/ns-allinone-3.21/ns-3.21/scratch
ln -s ~/NS3-SOP-Simulation/scratch/ ~/ns-allinone-3.21/ns-3.21/
ln -s ~/NS3-SOP-Simulation/qmysim ~/ns-allinone-3.21/ns-3.21/


rm ~/ns-allinone-3.21/ns-3.21/push-sop
rm ~/ns-allinone-3.21/ns-3.21/pull-sop
rm ~/ns-allinone-3.21/ns-3.21/mv-result
ln -s ~/NS3-SOP-Simulation/push-sop ~/ns-allinone-3.21/ns-3.21/
ln -s ~/NS3-SOP-Simulation/pull-sop ~/ns-allinone-3.21/ns-3.21/
ln -s ~/NS3-SOP-Simulation/mv-result ~/ns-allinone-3.21/ns-3.21/


git config --global user.email "s4582123@gmail.com"
git config --global user.name "HondaDai"

CXXFLAGS='-O3' ./waf configure -d optimized
CXXFLAGS='-O3' ./waf configure -d optimized