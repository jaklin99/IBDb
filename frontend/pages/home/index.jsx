import AppBar from "@mui/material/AppBar";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import CssBaseline from "@mui/material/CssBaseline";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Link from "@mui/material/Link";
import styles from "../../styles/Home.module.css";

const cards = [1, 2, 3];

export default function Home() {

  return (
    <div>
      <main>
        {/* Hero unit */}
        <Box
          sx={{
            bgcolor: "background.paper",
            pt: 12,
            pb: 6,
          }}
        >
          <Container maxWidth="sm">
            <Typography
              component="h2"
              variant="h2"
              align="center"
              color="#F7CCAC"
              gutterBottom
            >
              Start your reading journey
            </Typography>

            <Stack
              sx={{ pt: 4 }}
              direction="row"
              spacing={2}
              justifyContent="center"
            ></Stack>
          </Container>
          <Typography
            component="h6"
            variant="h6"
            align="center"
            color="#F7CCAC"
            gutterBottom
          >
            Choose your books
          </Typography>
        </Box>
        <Container sx={{ py: 8 }} maxWidth="md">
          {/* End hero unit */}
          <Grid container spacing={6}>
            {cards.map((card) => (
              <Grid item key={card} xs={2} sm={6} md={4}>
                <Card
                  sx={{
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                    backgroundColor: "#F7CCAC",
                  }}
                >
                  <CardMedia
                    component="img"
                    sx={{
                      pt: "20.25%",
                    }}
                    image="https://source.unsplash.com/random"
                    alt="random"
                  />
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                      <Link href="/" underline="none" color="#3A3845">
                        Heading
                      </Link>
                    </Typography>
                    <Typography color="#3A3845">Plot</Typography>
                  </CardContent>
                  <CardActions>
                    <Button size="small">
                      <Link href="/reviews" underline="none" color="#3A3845">
                        View reviews
                      </Link>
                    </Button>
                    <Button
                      size="small"
                      sx={{
                        color: "#3A3845",
                      }}
                    >
                      Add to wish list
                    </Button>
                  </CardActions>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Container>
      </main>
    </div>
  );
}
