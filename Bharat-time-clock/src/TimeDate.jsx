function TimeDate(){
  let time = new Date();

  return <p className="lead">The current date: {time.toLocaleDateString()} - time: {time.toLocaleTimeString()}</p>
}
export default TimeDate;