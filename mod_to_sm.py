import sys, os, shutil
from fnf_to_sm import main as fts

base_game = [ # PLEASE REPACKAGE YOUR MODS WITHOUT BASEGAME CONTENT!!!
	"blammed",
	"bopeebo",
	"cocoa",
	"dadbattle",
	"eggnog",
	"fresh",
	"high",
	"milf",
	"monster",
	"offsettest",
	"philly",
	"pico",
	"roses",
	"satin-panties",
	"senpai",
	"south",
	"spookeez",
	"test",
	"thorns",
	"tutorial",
	"winter-horrorland"
]

def main():
	in_dir = sys.argv[1]
	if not os.path.isdir(in_dir):
		raise NotADirectoryError(f"{in_dir} is not a directory")
		sys.exit(1)
	oggs = []
	oggdir = ""
	jsons = []
	jsondir = ""
	outdir = sys.argv[2] if len(sys.argv) >= 3 else "FNF Mods on Steroids"
	os.makedirs(outdir, exist_ok=True)
	for cdir, dirs, files in os.walk(in_dir):
		if (not (cdir.lower().endswith("manifest") or cdir.lower().endswith("images"))) and any([x for x in files if x.lower().endswith(".json")]):	
			jsons.append(os.path.basename(cdir).lower())
			jsondir = os.path.dirname(cdir)
		if any([x for x in files if x.lower() == "inst.ogg"]):
			oggs.append(os.path.basename(cdir).lower())
			oggdir = os.path.dirname(cdir)
	print(f"found oggfolder: {oggdir}")
	print(f"found jsonfolder: {jsondir}")
	songs = [x for x in jsons if x in oggs and x not in base_game]
	for song in songs:
		ogg = os.path.join(oggdir, song, "Inst.ogg")
		json = os.path.join(jsondir, song, f"{song}.json")
		if not os.path.isfile(json):
			# try a harder diff
			json = os.path.join(jsondir, song, f"{song}-hard.json")
			# still doesnt exist?
			if not os.path.isfile(json):
				# try an easier diff
				json = os.path.join(jsondir, song, f"{song}-easy.json")
		song_name = fts.get_songname(json)
		to = os.path.join(outdir, song_name)
		os.makedirs(to, exist_ok=True)
		fts.fnf_to_sm(json, os.path.join(to, song))
		shutil.copy(ogg, os.path.join(to, f"{song_name}.ogg"))

if __name__ == '__main__':
	main()