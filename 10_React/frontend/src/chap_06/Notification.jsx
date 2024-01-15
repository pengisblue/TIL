import React from "react";

// const styles = {
// };

class Notification extends React.Component {
  constructor(props) {
    super(props);

    this.state = {};
  }

  componentDidMount() {
    console.log(`${this.props.id} componentDidMount`);
  }

  componentDidUpdate() {
    console.log(`${this.props.id} componentDidUpdate`);
  }

  componentWillUnmount() {
    console.log(`${this.props.id} componentWillUnmount`);
  }

  render() {
    return (
      <div className="m-2 p-2 flex border border-solid border-gray-600 rounded-2xl">
        <span className="text-base text-black">{this.props.message}</span>
      </div>
    );
  }
}

export default Notification;