# Material-Design-Copier
A python script to copy content from a google material design folder into your android project. Requires python 2.7.7+ (python with argparse essentially)

#Usage

1. Make sure you have the material design assets folder downloaded from here: https://github.com/google/material-design-icons/releases/download/1.0.1/material-design-icons-1.0.1.zip
2. Place material-copy.py into the `material-design-icons` folder
3. Run `python material-copy.py <group> <name> <color> <dest>`

#Example:
```
(py2.7.10)$:~/material-design-icons-master$ python material-copy.py social poll white ~/workspace/some-project/res
Copying social/drawable-hdpi/ic_poll_white_48dp.png to ~/workspace/some-project/res/drawable-hdpi/ic_poll_white_48dp.png
Copying social/drawable-mdpi/ic_poll_white_48dp.png to ~/workspace/some-project/res/drawable-mdpi/ic_poll_white_48dp.png
Copying social/drawable-xhdpi/ic_poll_white_48dp.png to ~/workspace/some-project/res/drawable-xhdpi/ic_poll_white_48dp.png
Copying social/drawable-xxhdpi/ic_poll_white_48dp.png to ~/workspace/some-project/res/drawable-xxhdpi/ic_poll_white_48dp.png
Creating ~/workspace/some-project/res/drawable-xxxhdpi
Copying social/drawable-xxxhdpi/ic_poll_white_48dp.png to ~/workspace/some-project/res/drawable-xxxhdpi/ic_poll_white_48dp.png
```
