import React from "react";
import Comment from "./Comment";

const comments = [
  {
    name: "홍길동",
    comment: "이것은 댓글 입니다."
  },
  {
    name: "한석봉",
    comment: "컴포넌트 공부 중"
  },
]


function CommentList(props) {
  return (
    <div>
      {comments.map((comment) => {
        return (
          <Comment name={comment.name} comment={comment.comment} />
        );
      })}
    </div>
  );
}

export default CommentList;