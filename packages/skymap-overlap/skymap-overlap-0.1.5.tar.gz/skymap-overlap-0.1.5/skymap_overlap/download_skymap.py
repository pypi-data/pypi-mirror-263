#!/usr/bin/env python
from __future__ import print_function
from ligo.gracedb.rest import GraceDb
import argparse
import sys

def download_skymap(id, db, args, use_bayestar_only=False):
	try:
		# Use LALInference skymap if possible, except when use_bayestar_only is set
		if not use_bayestar_only:
			r = db.files(id, "LALInference.fits.gz")
			if args.verbose:
				print("Using LALInference skymap for {0}".format(id), file=sys.stderr)
		else:
			raise TypeError
	except:
		try:
			r = db.files(id, "bayestar.fits.gz")
			if args.verbose:
				print("Using Bayestar skymap for {0}".format(id), file=sys.stderr)
		except:
			r = db.files(id, "subthreshold.bayestar.fits.gz")
			if args.verbose:
				print("Using subthreshold Bayestar skymap for {0}".format(id), file=sys.stderr)

	outfile = open("{0}_skymap.fits.gz".format(id), "wb")
	outfile.write(r.read())
	outfile.close()

def main():
	parser = argparse.ArgumentParser(description = "Download skymaps from a list of events")
	parser.add_argument("event", nargs="+", help = "A list of gravitational-wave events, can be either GID for GW event or SID for superevent")
	parser.add_argument("--bayestar", action="store_true", help="Use bayestar skymap only")
	parser.add_argument("--verbose", action = "store_true", help = "Be very verbose")
	args = parser.parse_args()
	# FIXME Make sure that you have a valid proxy
	client = GraceDb()

	for event_id in args.event:
		try:
			download_skymap(event_id, client, args, use_bayestar_only=args.bayestar)
		except:
			if args.verbose:
				print("Failed to download the skymap for {}".format(event_id), file=sys.stderr)
