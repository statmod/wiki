library(Rssa)

dist_clust_old <- function(roots, delta) {
  pdf(file = "tex/fig/signal_roots.pdf", width = 6.5, height = 4)
  plot(roots, asp = 1)
  dev.off()
  roots_data <- cbind(Re(roots), abs(Im(roots)))
  res_indices <- numeric(0)
  res_k <- numeric(0)

  max_k <- nrow(unique(roots_data))

  if (max_k == 1){
    return(list(F1 = 1:nrow(roots_data)))
  }

  k <- 2

  while(k <= min(max_k, nrow(roots_data) - 1)) {
    res <- kmeans(roots_data, centers = k, nstart = 10)

    if (res$tot.withinss / res$totss < delta) {
      res_k <- k
      res_indices <- res$cluster
      break
    }

    k <- k + 1
  }

  if (length(res_indices) == 0) {
    res_k <- nrow(roots_data)
    res_indices <- 1:res_k
  }

  groups <- list()
  for (i in 1:res_k) {
    clust_indices <- which(res_indices == i)
    groups[[paste0("F", i)]] <- clust_indices
  }
  return(groups)
}

dist_clust_table <- function(roots_table, 
                             delta) {
  set.seed(10)
  roots_data <- roots_table
  res_indices <- numeric(0)
  res_k <- numeric(0)

  if (is.null(ncol(roots_table)))
    roots_data <- matrix(roots_data, nrow = 1)
  max_k <- nrow(unique(roots_data))
  
  if (max_k == 0){
    return(numeric(0))
  }

  if (max_k == 1){
    return(rep(1, nrow(roots_table)))
  }

  k <- 2

  while(k <= min(max_k, nrow(roots_data) - 1)) {
    res <- kmeans(roots_data, centers = k, nstart = 10)

    if (res$tot.withinss / res$totss < delta) {
      res_k <- k
      res_indices <- res$cluster
      break
    }

    k <- k + 1
  }

  if (length(res_indices) == 0) {
    res_k <- nrow(roots_data)
    if (res_k == 1)
      res_indices <- 1
    else
      res_indices <- 1:res_k
  }

  return(res_indices)
}

dist_clust <- function(roots, 
                       delta) {
  roots_data <- cbind(Re(roots), abs(Im(roots)))

  split_mask <- (roots_data[,1] < 0) & (roots_data[,2] < 0.1) & roots_data[,2] > -0.1
  part1 <- roots_data[split_mask,]
  if (!is.matrix(part1))
    part1 <- matrix(part1, nrow=1, ncol=2)
  part2 <- roots_data[split_mask == FALSE,]
  if (!is.matrix(part2))
    part2 <- matrix(part2, nrow=1, ncol=2)
  
  if (length(part1) > 0)
    indices1 <- dist_clust_table(part1, 
                                 delta = delta)
  else
    indices1 <- numeric(0)
  
  indices2 <- dist_clust_table(part2, 
                               delta = delta)
 
  if (length(indices1) > 0)
    max_index1 <- max(indices1)
  else
    max_index1 <- 0
  indices2 <- indices2 + max_index1

  res_indices <- numeric(length(roots))
  
  res_indices[split_mask] <- indices1
  res_indices[split_mask == FALSE] <- indices2

  groups <- list()
  res_k <- max(res_indices)
  for (i in 1:res_k) {
    clust_indices <- which(res_indices == i)
    groups[[paste0("F", i)]] <- clust_indices
  }
  return(groups)
}

freq_clust <- function(roots, auto_trend_freq = 1 / 24) {
  freqs <- abs(Im(log(roots))) / 2 / pi
  trend_group <- which(freqs < auto_trend_freq)
  periodic_group <- which(freqs >= auto_trend_freq)
  if (length(trend_group) == 0)
    return (list(F1 = periodic_group))
  if (length(periodic_group) == 0)
    return (list(F1 = trend_group))
  return(list(F1 = trend_group, F2 = periodic_group))
}

clust_basis_general <- function(U, roots, 
                                type = c("hierarchial", "distance", "frequency"), 
                                k = 2, 
                                auto_trend_freq = 1 / 24, 
                                delta = 1e-3, 
                                h = NULL, 
                                order = FALSE) {
  ord <- order(abs(Arg(roots)))
  roots <- roots[ord]
  
  U <- U[, ord, drop = FALSE]
  
  stopifnot(length(k) == 1)
  
  # Check for argument k, k <= the number of roots with nonegative imagine part
  maxk <- sum(Im(roots) >= -.Machine$double.eps) # Maybe just Im >= 0?
  
  if ((length(roots) == 1) | (k > maxk))
    k <- 1
  
  groups <- numeric(0)
  if (type == "hierarchial") {
    d <- stats::dist(cbind(Re(roots), abs(Im(roots))), method = "euclidian") # TODO Use the proper distance from KDU
    
    hc <- hclust(d, method = "complete")
    
    idx <- cutree(hc, k = k, h = h)
    
    groups <- tapply(seq_along(idx), idx, identity)
    names(groups) <- paste("F", names(groups), sep = "") 
  } else if (type == "distance") {
    groups <- dist_clust(roots, 
                         delta = delta)
  } else {
    groups <- freq_clust(roots, auto_trend_freq)
  }
  
  for (group in groups) {
    group_vecs <- U[, group, drop = FALSE]
    U[, group] <- svd(cbind(Re(group_vecs),
                            Im(group_vecs)),
                      nu = length(group), nv = 0)$u
  }
  
  U <- Re(U)
  
  if (order) {
    U <- U[, unlist(groups), drop = FALSE]
    l <- sapply(groups, length)
    cl <- cumsum(c(0, l))
    groups <- lapply(seq_along(l), function(i) (cl[i] + 1) : cl[i+1])
  }

  list(basis = U, groups = groups)
}

eossa_new <- function(x,
                      nested.groups, 
                      clust_type = c("hierarchial", "distance", "frequency"),
                      k = 2,
                      delta = 1e-3,
                      auto_trend_freq = 1 / 24,
                      subspace = c("column", "row"),
                      dimensions = NULL,
                      solve.method = c("ls", "tls"),
                      beta = 8,
                      ...) {
  if (missing(nested.groups))
    nested.groups <- as.list(1:min(nsigma(x), nu(x)))
  
  subspace <- match.arg(subspace)
  solve.method <- match.arg(solve.method)
  
  # Continue decomposition, if necessary
  Rssa:::.maybe.continue(x, groups = nested.groups, ...)
  
  idx <- sort(unique(unlist(nested.groups)))
  triples <- Rssa:::.get.orth.triples(x, idx, do.orthogonalize = FALSE)
  osigma <- triples$sigma; U <- triples$U; V <- triples$V
  
  if (identical(subspace, "column")) {
    vectors <- U
    V <- V * rep(osigma, each = nrow(V))
    wmask <- Rssa:::.wmask(x)
  } else if (identical(subspace, "row")) {
    vectors <- V
    U <- U * rep(sqrt(osigma), each = nrow(U))
    wmask <- Rssa:::.fmask(x)
  }
  sigma <- rep(1, length(idx))
  
  if (is.null(dimensions)) {
    dimensions <- seq_len(Rssa:::.dim(x))
  }
  
  d <- dim(wmask)
  
  if (max(dimensions) > length(d)) {
    stop(sprintf("some of input dimension indices exceed the actual number of object dimensions (%d)",
                 length(d)))
  }
  
  Zs <- lapply(dimensions,
               function(ndim) {
                 Rssa:::.shift.matrix(vectors,
                                      wmask = wmask,
                                      ndim = ndim,
                                      circular = x$circular[ndim],
                                      solve.method = solve.method)
               })
  
  Z <- Rssa:::.matrix.linear.combination(Zs, beta)
  Ze <- eigen(Z, symmetric = FALSE)
  
  # sm <- 0.5 * (Usm + t(Vsm)) # TODO implement two-sided ESPRIT????
  mb <- clust_basis_general(Ze$vectors, Ze$values,
                            type = clust_type,
                            k = k, 
                            delta = delta,
                            auto_trend_freq = auto_trend_freq)
  C <- mb$basis
  nested.groups <- mb$groups
  
  U <- U %*% C
  # V <- V %*% solve(t(C))  # TODO Use qr.solve here
  V <- t(qr.solve(C, t(V)))
  
  x <- clone(x, copy.cache = FALSE) # TODO Maybe we should to preserve the relevant part of the cache?
  Rssa:::.save.oblique.decomposition(x, sigma, U, V, idx)
  
  # Return to real group numbers
  nested.groups <- lapply(nested.groups, function(group) idx[group])
  
  # Grab old iossa.groups.all value
  iossa.groups.all <- Rssa:::.get(x, "iossa.groups.all", allow.null = TRUE)
  if (is.null(iossa.groups.all)) {
    iossa.groups.all <- list()
  }
  
  valid.groups <- as.logical(sapply(iossa.groups.all,
                                    function(group) length(intersect(group, idx)) == 0))
  Rssa:::.set(x, "iossa.groups",  nested.groups)
  Rssa:::.set(x, "iossa.groups.all", c(nested.groups, iossa.groups.all[valid.groups]))
  
  # Save nested components
  Rssa:::.set(x, "ossa.set", idx)
  
  if (!is.null(Rssa:::.decomposition(x, "nPR"))) {
    if (any(idx <= Rssa:::.decomposition(x, "nPR"))) {
      Rssa:::.set.decomposition(x, nPR = 0, nPL = 0)
    } else if (any(idx <= sum(unlist(Rssa:::.decomposition(x, c("nPR", "nPL")))))){
      Rssa:::.set.decomposition(x, nPL = 0)
    }
  }
  
  if (!inherits(x, "ossa")) {
    class(x) <- c("ossa", class(x))
  }
  
  # Save call info
  x$call <- match.call()
  
  invisible(x)
}