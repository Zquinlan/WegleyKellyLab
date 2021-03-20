#Make this work from command line
import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('currentDirectory', help='Github Directory')
parser.add_argument('infile', help='File to parse')
args = parser.parse_args()

class editPhotoAlbum():
    def __init__(self, args):
        super().__init__()
        self.currentDirectory = args['currentDirectory']
        self.logo = args['logo']

        with open(str(self.currentDirectory + '/docs/photos/curacao.md'), 'w+') as fout:
            frontmatter = str('---\nlayout: splash\nheader: \noverlay_color: "#5e616c"\noverlay_image: ' + self.logo + '\nsidebar:\n  nav: "content" \n')
            fout.write(frontmatter)
            
            fout.write('gallery:\n')

            children = []

            for root, dirs, files in os.walk(str(self.currentDirectory + '/docs/photos/curacao/')):
                files = [f for f in files if not f[0] == '.']
                pics = [f for f in files if not f.endswith(('.mov', '.mp4'))]

                for f in pics:
                    url = str('/docs/photos/curacao/' + f + '\n')

                    fout.write(str(' - image_path: ' + url))

            fout.write('\n---\n{% include gallery%}')

#For testing purposes

if __name__ == '__main__':
    createArgs = {'currentDirectory' :  '/Users/zacharyquinlan/Documents/Github/WegleyKellyLab', 'logo': '', 'photoAlbum' : '/Users/zacharyquinlan/Documents/temp.nosync/album', 'doi' : 'test'} 
    editPhotoAlbum(args = createArgs)
