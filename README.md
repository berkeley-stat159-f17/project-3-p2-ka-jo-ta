# TO DO

- Create environment
    * Needs to include pip installation for linear models, and a bunch of other stuff (see data_exploration notebook)

- Add watermark somehwere

- Add discussion of specialized secondary schools in Europe in both main and data_exploration notebooks

- Add some notes about the violin plots in the data_exploration notebook
    * The last two violin plots show that GP school students with low G3 scores seem to have higher G2 and G1 scores, indicative of some kind of bias (easier tests for G2/G1 in GP school? - probably not bc its only in the low end of G3… I’d guess that G3 covers some topics that were not as heavily covered in GP school, which would decrease grade of G3 independent of how well you do in G1/2, meaning that low G3 would have high G1/G2’s?)
    * Might be a remnant of the specialization that secondary schools in europe experience

- Figure out if we can make the output of the violin plots one big chunk, instead of scrolling through it

- Add functions and tests for the functions (REQUIRED FOR THIS PROJECT) (we need to think about what we can do that would require testable functions)

- Check how often we see `close_to_home` and the covariances with other variables (add this to the end of the analysis notebook [?] or maybe to the model_fitting notebook [?])
    * Then decide if we should interact with `travel_time` as instrument
    * Also need to add indicators for the different levels of `travel_time` and `reason`

- Add cluster robust SE's to the second regression, clustering by school

- Remove school as an instrument, not valid

- I think we need to move all the discussion of the models to the main.ipynb, which means we need to find a way to print the summary of the models in main
    * We can just use model_fitting to fit the actual models and as include maybe a brief discussion of what we do, the deep analysis should be moved to main


~~~~~~~~ BELOW HERE IS ORINIGAL README ~~~~~~~~
# Your Title here

This readme should be written by you, providing a high-level summary for newcomers of what the repository is about, what's where, and what to do to either read the main article or run the various analyses.

You don't need to replicate your main scientific narrative here, a repository README is meant to convey to anyone who finds your repo a few high-level things, for example:

- Purpose of the repository.
- Basic instructions to use it: what to install, if any, what to run, etc.  This will vary a lot from repo to repo, so use your judgment.
- A brief description of what is where (e.g. what important directories are included).
- Licensing conditions.

Look around on Github for inspiration on what people include in their READMEs that you find useful and informative. The [Reproducible Research section](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#reproducible-academic-publications) of the Jupyter Notebook Gallery includes a number of research-oriented links that may be useful.
