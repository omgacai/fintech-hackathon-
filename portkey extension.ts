//to run command in terminal
//npm install @portkey/detect-provider

import detectProvider from '@portkey/detect-provider';

// ES6 Async/Await syntax
async function main() {
  try {
    // Detect the provider
    const provider = await detectProvider();

    // Check if provider is available
    if (provider) {
      // Do something with the provider
      const accounts = await provider.request({ method: 'requestAccounts' });
      console.log(accounts);

      // Get the chain
      const chain = await provider.getChain('AELF');

      // Get the chain status
      const status = await chain.getChainStatus();
      console.log(status);

      // Get the contract (from aelf smart contract website)
      const tokenC = await chain.getContract('ELF_2FGMBFe58zu6WCDmxTbQtcgVrtjRK41xpxomuxwjdWPEd4xumh_tDVW');

      // Transfer
      const reqTransfer = await tokenC.callSendMethod('Transfer', accounts.AELF?.[0] || '', {
        amount: 100000,
        symbol: 'ELF',
        to: 'xxx',
      });
      console.log(reqTransfer);

      // GetBalance
      const reqGetBalance = await tokenC.callViewMethod('GetBalance', {
        symbol: 'ELF',
        owner: 'owner',
      });
      console.log(reqGetBalance);
    } else {
      console.log('Please install Portkey!');
    }
  } catch (error) {
    // Handle errors
    console.error(error);
  }
}

// Call the main function
main();
