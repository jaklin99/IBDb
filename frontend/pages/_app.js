// import React from "react";
// import PropTypes from "prop-types";
// import { CacheProvider } from "@emotion/react";
import { ThemeProvider, CssBaseline } from "@mui/material";
// import "tailwindcss/tailwind.css";
// import createEmotionCache from "../utility/createEmotionCache";
import lightTheme from "../styles/theme/lightTheme";
import "tailwindcss/tailwind.css";

// import "../styles/globals.css";

// const clientSideEmotionCache = createEmotionCache();

// const MyApp = (props) => {
//   const { Component, emotionCache = clientSideEmotionCache, pageProps } = props;

//   return (
//     <CacheProvider value={emotionCache}>
//       <ThemeProvider theme={lightTheme}>
//         <CssBaseline />
//         <Component {...pageProps} />
//       </ThemeProvider>
//     </CacheProvider>
//   );
// };

// export default MyApp;

// MyApp.propTypes = {
//   Component: PropTypes.elementType.isRequired,
//   emotionCache: PropTypes.object,
//   pageProps: PropTypes.object.isRequired,
// };
import { SessionProvider } from "next-auth/react";
export default function App({
  Component,
  pageProps: { session, ...pageProps },
}) {
  return (
    <ThemeProvider theme={lightTheme}>
      <SessionProvider session={session}>
        <CssBaseline />
        <Component {...pageProps} />
      </SessionProvider>
    </ThemeProvider>
  );
}
