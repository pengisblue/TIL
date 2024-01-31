import React from "react";

// const styles = {
// };

function Comment(props) {
  return (
    <div className="m-2 p-2 flex border border-solid border-gray-700 rounded-2xl">
      <div className="">
        <img
          className="w-12 h-12 rounded-full"
          src="https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png" 
          alt="profileImage" 
        />
      </div>

      <div className="ms-2 flex flex-col justify-center">
        <span className="text-base font-bold text-black">
          {props.name}
        </span>
        <span className="text-base text-black">
          {props.comment}
        </span>
      </div>
    </div>
  );
}

export default Comment;