// Hez_code Undercover Mode
// Prevents AI fingerprints, strips attribution, and evades detection

export class UndercoverMode {
  constructor(private enabled: boolean) {}

  public sanitize(output: string): string {
    if (!this.enabled) return output;
    // Strip AI fingerprints, attribution, and sensitive info
    let sanitized = output
      .replace(/Hez_code/g, 'Anonymous')
      .replace(/Claude Code/g, 'Anonymous')
      .replace(/AI/g, 'User')
      .replace(/Co-Authored-By:/g, '');
    return sanitized;
  }
}