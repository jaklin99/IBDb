// import * as React from "react";
// import Avatar from "@mui/material/Avatar";
// import Button from "@mui/material/Button";
// import TextField from "@mui/material/TextField";
// import Link from "@mui/material/Link";
// import Paper from "@mui/material/Paper";
// import Box from "@mui/material/Box";
// import Grid from "@mui/material/Grid";
// import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
// import Typography from "@mui/material/Typography";
// import { createTheme, ThemeProvider } from "@mui/material/styles";
// import LoginPic from "../../assets/IBDb-logos.jpeg";
// import { useState } from "react";
// import { useRouter } from "next/router";

// // const theme = createTheme();

// export default function SignInSide() {
//   // const handleSubmit = (event) => {
//   //   event.preventDefault();
//   //   const data = new FormData(event.currentTarget);
//   //   console.log({
//   //     email: data.get("email"),
//   //     password: data.get("password"),
//   //   });
//   // };
//  const [username, setUsername] = useState("");
//   const [password, setPassword] = useState("");
//   const router = useRouter();

//   function handleUsernameChange(e) {
//     setUsername(e.target.value);
//   }

//   function handlePasswordChange(e) {
//     setPassword(e.target.value);
//   }

//   async function handleSubmit(e) {
//     e.preventDefault();
//     const formData = new FormData();
//     formData.append("username", username);
//     formData.append("password", password);
//     const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/token`, {
//       method: "POST",
//       body: formData,
//     });
//     if (res.status == 200) {
//       const json = await res.json();
//       localStorage.setItem("token", json.access_token);
//       router.push("admin");
//     } else {
//       alert("Login failed.");
//     }
//   }
//   return (
//       <Grid container component="main" sx={{ height: "100vh" }}>
//         <Grid
//           item
//           xs={false}
//           sm={4}
//           md={7}
//           sx={{
//             backgroundImage: `url(${LoginPic})`,
//             backgroundRepeat: "no-repeat",
//             backgroundColor: (t) =>
//               t.palette.primary.main,
//             backgroundSize: "cover",
//             backgroundPosition: "center",
//           }}
//         />
//         <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
//           <Box
//             sx={{
//               my: 8,
//               mx: 4,
//               display: "flex",
//               flexDirection: "column",
//               alignItems: "center",
//             }}
//           >
//             <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
//               <LockOutlinedIcon />
//             </Avatar>
//             <Typography component="h1" variant="h5">
//               Sign in
//             </Typography>
//             <Box
//               component="form"
//               noValidate
//               onSubmit={handleSubmit}
//               sx={{ mt: 1 }}
//             >
//               <TextField
//                 margin="normal"
//                 required
//                 fullWidth
//                 id="email"
//                 label="Email Address"
//                 name="email"
//                 autoComplete="email"
//                 autoFocus
//                 value={username}
//                 onChange={handleUsernameChange}
//               />
//               <TextField
//                 sx={{ color: "#3A3845" }}
//                 margin="normal"
//                 required
//                 fullWidth
//                 name="password"
//                 label="Password"
//                 type="password"
//                 id="password"
//                 autoComplete="current-password"
//                 value={password}
//                 onChange={handlePasswordChange}
//               />

//               <Button
//                 type="submit"
//                 fullWidth
//                 sx={{
//                   mt: 3,
//                   mb: 2,
//                   backgroundColor: "#F7CCAC",
//                   color: "#3A3845",
//                 }}
//               >
//                 Sign In
//               </Button>
//               <Grid container>
//                 <Grid item>
//                   <Link href="#" variant="body2" color="#3A3845">
//                     {"Don't have an account? Sign Up"}
//                   </Link>
//                 </Grid>
//               </Grid>
//             </Box>
//           </Box>
//         </Grid>
//       </Grid>
//   );
// }

// // export default function Login() {
// //   const [username, setUsername] = useState("");
// //   const [password, setPassword] = useState("");
// //   const router = useRouter();

// //   function handleUsernameChange(e) {
// //     setUsername(e.target.value);
// //   }

// //   function handlePasswordChange(e) {
// //     setPassword(e.target.value);
// //   }

// //   async function handleSubmit(e) {
// //     e.preventDefault();
// //     const formData = new FormData();
// //     formData.append("username", username);
// //     formData.append("password", password);
// //     const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/token`, {
// //       method: "POST",
// //       body: formData,
// //     });
// //     if (res.status == 200) {
// //       const json = await res.json();
// //       localStorage.setItem("token", json.access_token);
// //       router.push("admin");
// //     } else {
// //       alert("Login failed.");
// //     }
// //   }

// //   return (
// //     <>
// //       <div className="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
// //         <div className="max-w-md w-full space-y-8">
// //           <div>
// //             <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
// //               Sign in to your account
// //             </h2>
// //           </div>
// //           <form
// //             className="mt-8 space-y-6"
// //             action="#"
// //             method="POST"
// //             onSubmit={handleSubmit}
// //           >
// //             <input type="hidden" name="remember" defaultValue="true" />
// //             <div className="rounded-md shadow-sm -space-y-px">
// //               <div>
// //                 <label htmlFor="username" className="sr-only">
// //                   Username
// //                 </label>
// //                 <input
// //                   id="username"
// //                   name="username"
// //                   type="text"
// //                   autoComplete="username"
// //                   required
// //                   className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
// //                   placeholder="Username"
// //                   value={username}
// //                   onChange={handleUsernameChange}
// //                 />
// //               </div>
// //               <div>
// //                 <label htmlFor="password" className="sr-only">
// //                   Password
// //                 </label>
// //                 <input
// //                   id="password"
// //                   name="password"
// //                   type="password"
// //                   autoComplete="current-password"
// //                   required
// //                   className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
// //                   placeholder="Password"
// //                   value={password}
// //                   onChange={handlePasswordChange}
// //                 />
// //               </div>
// //             </div>

// //             <div className="flex items-center justify-between">
// //               <div className="flex items-center">
// //                 <input
// //                   id="remember-me"
// //                   name="remember-me"
// //                   type="checkbox"
// //                   className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
// //                 />
// //                 <label
// //                   htmlFor="remember-me"
// //                   className="ml-2 block text-sm text-gray-900"
// //                 >
// //                   Remember me
// //                 </label>
// //               </div>

// //               <div className="text-sm">
// //                 <a
// //                   href="#"
// //                   className="font-medium text-indigo-600 hover:text-indigo-500"
// //                 >
// //                   Forgot your password?
// //                 </a>
// //               </div>
// //             </div>

// //             <div>
// //               <button
// //                 type="submit"
// //                 className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
// //               >
// //                 <span className="absolute left-0 inset-y-0 flex items-center pl-3"></span>
// //                 Sign in
// //               </button>
// //             </div>
// //           </form>
// //         </div>
// //       </div>
// //     </>
// //   );
// // }

// import React from "react";
// import { NextPage } from "next";
// import Login_ from "../../components/login_btn";

// function Login() {
//   return <Login_></Login_>;
// }

// export default Login;
import Head from "next/head";
import styles from "../../styles/pageStyles/login.module.css";
import { useState, useEffect } from "react";
import { useRouter } from "next/router";
import { signIn, useSession } from "next-auth/react";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoginStarted, setIsLoginStarted] = useState(false);
  const [loginError, setLoginError] = useState("");
  const router = useRouter();

  useEffect(() => {
    if (router.query.error) {
      setLoginError(router.query.error);
      setEmail(router.query.email);
    }
  }, [router]);

  const handleLogin = (e) => {
    e.preventDefault();
    setIsLoginStarted(true);
    signIn("credentials", {
      email,
      password,
      callbackUrl: `${window.location.origin}/`,
    });
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>NextAuth Example</title>
      </Head>
      <main className={styles.loginMain}>
        <div className={styles.loginStep}>
          <h1>Welcome Back</h1>
          <form onSubmit={(e) => handleLogin(e)} className={styles.loginForm}>
            <label htmlFor="loginEmail">Email</label>
            <input
              id="loginEmail"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={loginError ? styles.errorInput : ""}
            />
            <span className={styles.error}>{loginError}</span>
            <label htmlFor="inputPassword">Password</label>
            <input
              id="inputPassword"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button
              type="submit"
              disabled={isLoginStarted}
              className={styles.blueButtonRound}
            >
              Log In
            </button>
          </form>
        </div>
      </main>
    </div>
  );
}
