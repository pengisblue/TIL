function hell (win) {
  return function () {
    loadLink(win, REMOTE_SRC, function () {
      loadLink(win, REMOTE_SRC, function () {
        loadLink(win, REMOTE_SRC, function () {
          loadLink(win, REMOTE_SRC, function () {
            loadLink(win, REMOTE_SRC, function () {
              loadLink(win, REMOTE_SRC, function () {
              })
            })
          })
        })
      })
    })
  }
}
