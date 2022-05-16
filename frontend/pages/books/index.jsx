// import AppBar from '@mui/material/AppBar';
// import Button from '@mui/material/Button';
// import CameraIcon from '@mui/icons-material/PhotoCamera';
// import Card from '@mui/material/Card';
// import CardActions from '@mui/material/CardActions';
// import CardContent from '@mui/material/CardContent';
// import CardMedia from '@mui/material/CardMedia';
// import CssBaseline from '@mui/material/CssBaseline';
// import Grid from '@mui/material/Grid';
// import Stack from '@mui/material/Stack';
// import Box from '@mui/material/Box';
// import Toolbar from '@mui/material/Toolbar';
// import Typography from '@mui/material/Typography';
// import Container from '@mui/material/Container';
// import Link from '@mui/material/Link';
// import { createTheme, ThemeProvider } from '@mui/material/styles';
// import {Header,Footer} from "../../components"

// import Head from "next/head";
// import { useState, useEffect } from "react";

//   const cards = [1, 2, 3];

//   export default function MyBooks() {
//     const [book, setBook] = useState("");
//   const [books, setBooks] = useState([]);

//   useEffect(() => {
//     async function fetchBooks() {
//       const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books/`);
//       const json = await res.json();
//       console.log(json);
//       setBooks(json);
//     }
//     fetchBooks();
//   }, []);

//   function handleChange(e) {
//     setBook(e.target.value);
//   }

//   async function handleSubmit() {
//     const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/books/add`, {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({
//         text: book,
//         completed: false,
//       }),
//     });
//     const json = await res.json();
//     setBooks([...books, json]);
//   }

//     return (
//       <div>
//         <Header />
//         <main>
//           {/* Hero unit */}
//           <Box
//             sx={{
//               bgcolor: "background.paper",
//               pt: 12,
//               pb: 6,
//             }}
//           >
//             <Container maxWidth="sm">
//               <Typography
//                 component="h1"
//                 variant="h2"
//                 align="center"
//                 color="text.primary"
//                 onChange={handleChange}
//                 gutterBottom
//               >
//                 My books
//               </Typography>

//               <Stack
//                 sx={{ pt: 4 }}
//                 direction="row"
//                 spacing={2}
//                 justifyContent="center"
//               ></Stack>
//             </Container>
//           </Box>
//           <Container sx={{ py: 8 }} maxWidth="md">
//             {/* End hero unit */}
//             <Grid container spacing={6}>
//               {cards.map((card) => (
//                 <Grid item key={card} xs={2} sm={6} md={4}>
//                   <Card
//                     sx={{
//                       height: "100%",
//                       display: "flex",
//                       flexDirection: "column",
//                     }}
//                   >
//                     <CardMedia
//                       component="img"
//                       sx={{
//                         pt: "20.25%",
//                       }}
//                       image="https://source.unsplash.com/random"
//                       alt="random"
//                     />
//                     <CardContent sx={{ flexGrow: 1 }}>
//                       <Typography gutterBottom variant="h5" component="h2">
//                         Heading
//                       </Typography>
//                       <Typography>Plot</Typography>
//                     </CardContent>
//                     <CardActions>
//                       {/* <Button size="small">View reviews</Button> */}
//                       <Button size="small" onClick={handleSubmit}>
//                         Add to wish list
//                       </Button>
//                     </CardActions>
//                   </Card>
//                 </Grid>
//               ))}
//             </Grid>
//           </Container>
//         </main>
//         <ul>
//           {books &&
//             books.map((book) => (
//               <li
//                 key={book.id}
//                 className="bg-yellow-100 m-3 p-3 border-yellow-200 border-2"
//               >
//                 {book.text}
//               </li>
//             ))}
//         </ul>
//         <Footer />
//       </div>
//     );
//   }

import Head from "next/head";
import { useState, useEffect } from "react";

export default function Books() {
  const [book, setBook] = useState("");
  const [books, setBooks] = useState([]);

  useEffect(() => {
    async function fetchBooks() {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/books`);
      const json = await res.json();
      console.log(json);
      setBooks(json);
    }
    fetchBooks();
  }, []);

  function handleChange(e) {
    setBook(e.target.value);
  }

  async function handleSubmit() {
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/api/books/add`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: book.title,
          completed: false,
        }),
      }
    );
    const json = await res.json();
    setBooks([...books, json]);
  }

  return (
    <div>
      <Head>
        <title>Books</title>
      </Head>
      <div className="container mx-auto p-10 m-10">
        <div className="flex flex-col">
          <h1 className="font-bold mb-3">Books</h1>
          <textarea
            value={book.title}
            onChange={handleChange}
            className="border-2"
          ></textarea>
          <textarea
            value={book.genre}
            onChange={handleChange}
            className="border-2"
          ></textarea>
          <textarea
            value={book.year}
            onChange={handleChange}
            className="border-2"
          ></textarea>
          <div className="mx-auto p-3 m-5">
            <button
              onClick={handleSubmit}
              className="bg-green-500 p-3 text-white"
            >
              Submit
            </button>
          </div>
          <div>
            <ul>
              {books &&
                books.map((book) => (
                  <li
                    key={book.id}
                    className="bg-yellow-100 m-3 p-3 border-yellow-200 border-2"
                  >
                    {book.title}
                  </li>
                ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
