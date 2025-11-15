#!/usr/bin/env python

import argparse
import os
import subprocess

#import rjsmin
#def minify_rjsmin(fp_in, unminified):
#    return rjsmin.jsmin(unminified)

def minify_slimit(fp_in, unminified):
    return subprocess.check_output(["slimit", "-m", fp_in],
                                   stderr=subprocess.STDOUT
                                   ).decode("utf-8")

def minify_yuicompressor(fp_in, unminified):
    return subprocess.check_output(["java", "-jar", os.path.expanduser("~/bin/yuicompressor-2.4.8.jar"), fp_in],
                                   stderr=subprocess.STDOUT
                                   ).decode("utf-8")

def minify_crimp(fp_in, unminified):
    return subprocess.check_output(["crimp", fp_in, "-m"],
                                   stderr=subprocess.STDOUT
                                   ).decode("utf-8")

def minify_uglify(fp_in, unminified):
    return subprocess.check_output(["uglifyjs", fp_in, "-m", "-c"],
                                   stderr=subprocess.STDOUT
                                   ).decode("utf-8")

minifiers = [
    # used for static/js/sh
    { "name": "slimit", "func": minify_slimit, "count": 0, "errors": 0 },

    # used for static/js
    { "name": "uglify", "func": minify_uglify, "count": 0, "errors": 0 },

    # not giving any useful results
    #{ "name": "rjsmin", "func": minify_rjsmin, "count": 0, "errors": 0 },
    #{ "name": "yuicompressor", "func": minify_yuicompressor, "count": 0, "errors": 0 },
    #{ "name": "crimp", "func": minify_crimp, "count": 0, "errors": 0 },
]

saved = 0

def minify_file(fp_in, fp_out):
    global saved

    with open(fp_in, "r") as f:
        unminified = f.read()

    minified = ""
    unminified_lines = unminified.split("\n")

    if unminified_lines[0].startswith("// @license"):
        minified += unminified_lines[0] + "\n"

    mini = ""
    mini_select = None
    for i, f in enumerate(minifiers):
        try:
            m = f["func"](fp_in, unminified)
            print(fp_in + " with " + f["name"] + " at " + str(len(m)))
            if (len(mini) == 0) or (len(m) < len(mini)):
                mini = m
                mini_select = i
        except Exception as e:
            print("could not convert " + fp_in + " with " + f["name"])
            #print(e)
            f["errors"] += 1

    if len(mini) == 0:
        print("ERROR: could not convert " + fp_in)
        return

    minifiers[mini_select]["count"] += 1
    print(fp_in + " used " + minifiers[mini_select]["name"] + " at " + str(len(mini)))
    minified += mini

    if unminified_lines[-2].startswith("// @license"):
        minified += "\n" + unminified_lines[-2] + "\n"

    minified = "\n".join([line for line in minified.split("\n") if len(line) > 0])

    saved += len(unminified) - len(minified)

    with open(fp_out, "w") as f:
        f.write(minified)

def minify_dir(dirpath):
    for filename in os.listdir(dirpath):
        if filename.endswith(".js") and not filename.endswith(".min.js"):
            fp_in = os.path.join(dirpath, filename)
            fp_out = os.path.splitext(fp_in)[0] + ".min.js"
            print("minify " + fp_in + " to " + fp_out)
            minify_file(fp_in, fp_out)
            print()

    for f in minifiers:
        print(f["name"] + " count=" + str(f["count"]) + " errors=" + str(f["errors"]))

    print("saved " + str(saved) + " bytes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="working directory", default=".")
    args = parser.parse_args()
    minify_dir(args.directory)
