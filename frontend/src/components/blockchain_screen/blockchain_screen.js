import { Container, Grid } from "@mui/material";
import { makeStyles } from "@mui/styles";
import React, { useEffect, useState } from "react";
import Header from "../header/header";
import Block from "./block";
import Chain from "./link";
import Main from './Main';

const useStyle = makeStyles((theme) => ({
  root: {},
  blockchain: {
    padding: 5,
  },
}));

function BlockChainScreen() {
  const classes = useStyle();


  const [blocks, setblocks] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://localhost:6500/get_chain");
      const result = await response.json();
      if (result) setblocks(result.chain);
    };
    fetchData();
  }, []);

  console.log(blocks);


  return (
    <>


      <Header />
      <br />
      <br />
      <br />

      <div>
      <Main />
    </div>

      <div>
         <br></br>
         <div
            class = "image"
            style = {{
               height: "200px",
               width: "450px",
               textAlign: "center",
               backgroundImage:
               'url("https://i.postimg.cc/jdhmFHh2/bg.png")',
               backgroundSize: "contain",
               backgroundRepeat: "no-repeat",
               display: "block",
               marginLeft: "auto",
               marginRight: "auto",
               
              //  width: "",
               position: "relative",
               top: "-55rem",
               
               marginBottom: "-55rem",
              
            }}
         >
         </div>


      </div>

    
      <Container>
        <Grid
          className={classes.blockchain}
          container
          spacing={5}
          alignItems={"center"}
          justifyContent={"center"}
        >
          {blocks.map((block) => (
            <>
              <Block key={block.index} block={block} />
              <Chain key={block.hash} />
            </>
          ))}
        </Grid>
      </Container>
    </>
  );
}

export default BlockChainScreen;
