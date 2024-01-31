import React from "react";
import Book from "./Book";

function Library(props) {
  return (
    <div>
      <Book name="python" numOfPage={300}/>
    </div>
  );
}

export default Library;