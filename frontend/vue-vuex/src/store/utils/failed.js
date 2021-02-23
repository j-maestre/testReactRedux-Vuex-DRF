export function failed(commit, error, msg) {
  let log = !error.response
    ? "Error server connection (Hablar con xema)"
    : Object.entries(error.response.data.errors).map(
        ([key, value]) => key + ": " + value
      );

  // ERROR
  msg
    ? commit(
        "SET_MSG",
        {
          type: false,
          title: msg,
          details: "" + log,
        },
        { root: true }
      )
    : false;

  return false;
}
