import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import Container from "@mui/material/Container";
import Link from "@mui/material/Link";
import FacebookRoundedIcon from "@mui/icons-material/FacebookRounded";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import InstagramIcon from "@mui/icons-material/Instagram";
import EmailIcon from "@mui/icons-material/Email";
import IconButton from "@mui/material/IconButton";

function Copyright() {
  return (
    <Box sx={{ textAlign: "center" }}>
      <Typography variant="body2" color="text.secondary">
        {"Copyright © "}
        <Link color="inherit" href="https://mui.com/">
          IBDb{" "}
        </Link>{" "}
        {new Date().getFullYear()}
        {"."}
      </Typography>
    </Box>
  );
}

export default function Footer() {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "50vh",
      }}
    >
      <Box
        component="footer"
        sx={{
          py: 3,
          px: 2,
          mt: "auto",
          backgroundColor: (theme) =>
            theme.palette.mode === "light"
              ? theme.palette.grey[200]
              : theme.palette.grey[800],
        }}
      >
        <Box sx={{ textAlign: "center" }}>
          <IconButton href="https://www.facebook.com/profile.php?id=100010174632072">
            <FacebookRoundedIcon />
          </IconButton>
          <IconButton href="https://www.linkedin.com/in/jaklin-yanakieva-4a5866201/">
            <LinkedInIcon />
          </IconButton>
          <IconButton href="https://www.instagram.com/_jkln_y_/">
            <InstagramIcon />
          </IconButton>
          <IconButton href="mailto:jakitoo99@gmail.com">
            <EmailIcon />
          </IconButton>
          <Stack>
            <Link variant="body2" href="/sign_up" color="inherit">
              Register for free
            </Link>
          </Stack>

          <Copyright />
        </Box>
      </Box>
    </Box>
  );
}
