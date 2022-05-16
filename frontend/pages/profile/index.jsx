// import { Header, Footer } from "../../components";
// import Card from "@mui/material/Card";
// import CardActions from "@mui/material/CardActions";
// import CardContent from "@mui/material/CardContent";
// import CardMedia from "@mui/material/CardMedia";
// import Button from "@mui/material/Button";
// import Typography from "@mui/material/Typography";
// import Tabs from "../../components/tabs";
// import { Container } from "@mui/material";
// import { flexbox } from "@mui/system";

// function MyProfile() {
//   return (
//     <div>
//       <Header />
//       <Container sx={{ flexGrow: 1, padding: 10, display: "flex" }}>
//         <Card sx={{ height: 700 }}>
//           <CardMedia
//             component="img"
//             alt="green iguana"
//             height="140"
//             image="/static/images/cards/contemplative-reptile.jpg"
//           />
//           <CardContent>
//             <Typography gutterBottom variant="h5" component="div">
//               Name
//             </Typography>
//             <Typography variant="body2" color="text.secondary">
//               email
//             </Typography>
//             <Typography variant="body2" color="text.secondary">
//               phone
//             </Typography>
//           </CardContent>
//           <CardActions>
//             <Button size="small">Edit</Button>
//             <Button size="small">Logout</Button>
//           </CardActions>
//         </Card>
//         <Tabs />
//       </Container>
//       <Footer />
//     </div>
//   );
// }
// export default MyProfile;


import { useNavigate } from "react-router";
export default function Profile() {
  const navigate = useNavigate();

  const signOut = () => {
    localStorage.removeItem("temitope");
    navigate("/");
  };

  return (
    <>
      <div style={{ marginTop: 20, minHeight: 700 }}>
        <h1>Profile page</h1>
        <p>Hello there, welcome to your profile page</p>

        <button onClick={signOut}>sign out</button>
      </div>
    </>
  );
}