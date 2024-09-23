largeWASMcheck=function(path){
  packages_path=paste0(path,"/shinylive/webr/packages/")
  packages_path <- sprintf(packages_path)
  
  # remove the dirs with size >= 100 MB
  for (x in list.dirs(packages_path)) {
    x_files <- file.info(list.files(x, full.names = TRUE))
    if (any(x_files$size > 100 * 1024^2)) {
      print(x)
      unlink(x, recursive = TRUE)
    }
  }
  
  # refresh the `metadata.rds` file
  metadata_path <- file.path(packages_path, "metadata.rds")
  metadata <- readRDS(metadata_path)
  new_metadata <- metadata[intersect(names(metadata), list.dirs(packages_path, full.names = FALSE))]
  saveRDS(new_metadata, metadata_path)
}

# system.file("examples", "01_hello", package="shiny") |>
#   fs::dir_copy("App1", overwrite = TRUE)
# 
# system.file("examples", "03_reactivity", package="shiny") |>
#   fs::dir_copy("App2", overwrite = TRUE)

# App1 -- test
setwd("~/Dropbox/GitHub/ShinyApps/App1")
shinylive::export(".", "shinylive")
largeWASMcheck("shinylive")

# App2 -- test
setwd("~/Dropbox/GitHub/ShinyApps/App2")
shinylive::export(".", "shinylive")
largeWASMcheck("shinylive")

# Sequencing Estimator
setwd("~/Dropbox/GitHub/ShinyApps/SequencingEstimator/")
shinylive::export(".","shinylive")
largeWASMcheck("shinylive")

# Project Planner
setwd("~/Dropbox/GitHub/ShinyApps/ProjectPlanner/")
shinylive::export(".","shinylive")
largeWASMcheck("shinylive")

# CoordinateMapper
setwd("~/Dropbox/GitHub/ShinyApps/CoordinateMapper/")
shinylive::export(".","shinylive")
largeWASMcheck("shinylive")
